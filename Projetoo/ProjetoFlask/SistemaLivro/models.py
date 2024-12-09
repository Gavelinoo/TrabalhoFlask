'''Este arquivo é responsável pela estrutura do banco de dados'''
from ProjetoFlask.SistemaLivro import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader # função que carrega o usuario
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario)) # busca a informação do usuario

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    # nao e coluna, so uma relacao, aponta somente para a tabela de livros, atraves do usuario
    livros = database.relationship("Foto", backref="usuario", lazy=True) # o backref associa a foto ao usuario
    pass

class Livros(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    # a capa é armazenada em texto pois a info é o nome da img onde o arquivo esta
    capa = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    pass