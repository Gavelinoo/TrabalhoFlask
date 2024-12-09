"""Esse arquivo cria o app"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt




app = Flask(__name__) # chama a classe Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "a4c649b5832ad6a035ad93754af104d4"

database = SQLAlchemy(app) ## cria o banco de dados, usando o app criado
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"



# devida a referencia circular, importa o routes depois do app criado
from ProjetoFlask.SistemaLivro import routes
