from flask import Blueprint, request, render_template, \
    session, send_file
from DNA_protein import translacja
from DNA_reverse_RNA import zmieniaj
from datetime import datetime
from zapis_do_json import zapisuje_json
from auth import login_required
import json
from db_utils import get_connection

DNA_bp = Blueprint('DNA_endpoints', __name__)

@DNA_bp.route('/')
@login_required
def podaj_nazwe():
    username = session.get('username')
    return render_template('podaj_nazwe.html', username=username)

@DNA_bp.route('/przeglad')
@login_required
def przeglad():
    username = session.get('username')
    is_admin = session.get('is_admin')

    conn = get_connection()
    c = conn.cursor()

    if is_admin:
        result = c.execute('SELECT * FROM sekwencje JOIN users ON sekwencje.user_id = users.username')
    else:
        result = c.execute('SELECT * FROM sekwencje WHERE user_id = ?', (username,))

    zawartosc = result.fetchall()

    context = {
        'username': username,
        'zawartosc': zawartosc,
        'is_admin': is_admin
    }

    return render_template('przeglad.html', **context)

@DNA_bp.route('/podaj')
@login_required
def podaj_DNA():
    username = session.get('username')

    conn = get_connection()
    c = conn.cursor()

    result = c.execute('SELECT nazwa FROM sekwencje WHERE user_id = ?', (username,))
    zawartosc = result.fetchall()
    nazwy = []
    for row in zawartosc:
        nazwy.append(row['nazwa'])

    nazwa_projektu = request.args.get('name')
    if not nazwa_projektu:
        return render_template('error_no_input_nazwa.html')
    elif nazwa_projektu in nazwy:
        return render_template('error_project_name_exists.html')

    else:
        czas = datetime.now()
        data = str(czas.date())
        godzina = str(czas.time())
        dane = {'nazwa': nazwa_projektu, 'data': data, 'godzina': godzina}

        with open('Wpis.json', 'w') as f:
            json.dump(dane, f)

        return render_template('podaj_DNA.html', username=username)

@DNA_bp.route('/wybor')
@login_required
def wybierz_opcje():
    username = session.get('username')
    sekwencja = request.args.get('sequence')
    if sekwencja == "Tu wpisz sekwencję DNA":
        return render_template('error_no_input.html')

    sekwencja = sekwencja.upper()
    while True:
        for n in sekwencja:
            if n not in ['A', 'T', 'C', 'G']:
                return render_template('error.html')

        with open('Sekwencja.txt', mode='w') as f:
                f.write(sekwencja)

        sekwencja_slownik = {'sekwencja_wejscie': sekwencja}
        zapisuje_json(sekwencja_slownik)

        return render_template('wybor_opcji.html', dane=sekwencja, username=username)


@DNA_bp.route('/zmiana')
@login_required
def zmien():
    id = session.get('user_id')
    username = session.get('username')

    dane_uzytkownika = {'id': id, 'username': username}
    zapisuje_json(dane_uzytkownika)

    komplementarne_kod = {'A': 'T',
                      'T': 'A',
                      'G': 'C',
                      'C': 'G'}

    RNA_kod = {'A': 'A',
           'T': 'U',
           'G': 'G',
           'C': 'C'}
    wybor = request.args.get('typ')
    wybor_dict = {'rodzaj_zmiany': wybor}
    zapisuje_json(wybor_dict)

    with open('Sekwencja.txt', mode='r') as f:
        sekw = f.read()
        zmieniona = ''

        if wybor == 'RNA':
            zmieniona = zmieniaj(sekw, RNA_kod)
            zmiana = 'RNA'

        elif wybor == 'reverse':
            zmieniona = zmieniaj(sekw, komplementarne_kod)
            zmiana = 'DNA nić odwrócona'

        elif wybor == 'protein':
            zmieniona = translacja(sekw)
            zmiana = 'Białko'

    zmieniona_dict = {'sekwencja_wyjscie': zmieniona}

    with open('Rezultat.txt', mode='w') as f:
        f.write(zmieniona)
    zapisuje_json(zmieniona_dict)
    with open('Wpis.json') as f:
        wpis = json.load(f)
        zapytanie = """INSERT INTO 'sekwencje' VALUES (NULL, :username, :nazwa, :sekwencja_wejscie, :rodzaj_zmiany, :sekwencja_wyjscie, :data, :godzina); """
        conn = get_connection()
        c = conn.cursor()
        c.execute(zapytanie, wpis)
        conn.commit()
        conn.close()

    return render_template('zmien.html', dane=zmieniona, sekwencja=sekw, zmiana=zmiana, username=username)

@DNA_bp.route('/plik_wynik')
@login_required
def plik_wynik():
    return send_file('Rezultat.txt', as_attachment=True)

@DNA_bp.route('/plik_sekwencja')
@login_required
def plik_sekwencja():
    return send_file('Sekwencja.txt', as_attachment=True)
