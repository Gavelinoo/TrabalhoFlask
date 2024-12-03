"""Esse arquivo cria o app"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # chama a classe Flask

# devida a referencia circular, importa o routes depois do app criado
from ProjetoFlask.SistemaLivro import routes
