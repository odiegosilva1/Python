from flask import Flask
from db import db
from models import Usuario

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # CORREÇÃO 2: Formato correto da URI

# Inicializa o db com o app
db.init_app(app)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas
        print("Banco de dados criado com sucesso!")
    app.run(debug=True)