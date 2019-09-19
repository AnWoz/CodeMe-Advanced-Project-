from flask import Flask
from auth import auth_bp
from DNA import DNA_bp

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'
app.register_blueprint(auth_bp)
app.register_blueprint(DNA_bp)



if __name__ == "__main__":
    app.run(debug=True)
