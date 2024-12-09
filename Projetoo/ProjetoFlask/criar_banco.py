from ProjetoFlask.SistemaLivro import database, app
from ProjetoFlask.SistemaLivro.models import Usuario, Livros # importa as duas classes pras tabelas

with app.app_context():
    database.create_all()