from werkzeug.security import generate_password_hash

if __name__ == '__main__':
    password = input('Podaj hasło: ')

    hashed_password = generate_password_hash(password)
    print(f'{password} -> {hashed_password}')
