from werkzeug.security import generate_password_hash
from db_utils import get_connection

def dodaj_uzytkownika(username, hashed_password, is_admin):
    conn = get_connection()
    c = conn.cursor()
    dane = {'username': username, 'password': hashed_password, 'is_admin': is_admin}
    zapytanie = """INSERT INTO 'users' VALUES (NULL, :username, :password, :is_admin); """
    c.execute(zapytanie, dane)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    username = input('Podaj nazwę użytkownika: ')

    password = input('Podaj hasło: ')

    hashed_password = generate_password_hash(password)
    print(f'{password} -> {hashed_password}')

    czy_admin = input('Czy ma uprawnienia administratora?[T/N]')

    czy_admin = czy_admin.upper()
    if czy_admin == 'T':
        is_admin = 1
    elif czy_admin == 'N':
        is_admin = 0
    else:
        print('Wybierz poprawną wartość: T lub N!')
    print(username, hashed_password, is_admin)

    dodaj_uzytkownika(username, hashed_password, is_admin)

