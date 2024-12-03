'''Este arquivo guarda todas as rotas'''
from flask import render_template, url_for  ## procura a pasta dos templates
from ProjetoFlask.SistemaLivro import app

@app.route("/") # decorator, adiciona uma funcionalidade extra para a função abaixo
def homepage():
    return render_template("homepage.html")  # valor que ta no link vai ser parametro

##todo Associar o nome do usuario automaticamente

@app.route("/reservar") # nome dentro da chave carrega o usuario na url
def reservar(): # função recebe o usuario como variavel
    return render_template("reservar.html")  #passa o parametro para o html

@app.route("/devolver")
def devolver():
    return render_template("devolver.html")






