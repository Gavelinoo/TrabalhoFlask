"""Esse arquivo cria as bases do site, autenticação, banco de dados """
from ProjetoFlask.SistemaLivro import app
# from SistemaLivro.estruturas import FilaLigada
# # Banco de dados
# livros = {
#     "1234": {"titulo": "Python Básico", "fila": FilaLigada(), "disponivel": True},
#     "5678": {"titulo": "Estruturas de Dados", "fila": FilaLigada(), "disponivel": True},
# }

if __name__ == "__main__": # só roda o código se tiver usando diretamente o arquivo
    app.run(debug=True)
