import json

def zapisuje_json(dane):
    with open('Wpis.json') as f:
        zawartosc = json.load(f)
        for x, y in dane.items():
            zawartosc[x] = y

    with open('Wpis.json', 'w') as f:
        json.dump(zawartosc, f)
