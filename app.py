from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Desafio Cumprido - Caique Freitas"

if __name__ == '__main__':
    app.run()
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)