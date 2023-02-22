from flask import Flask, render_template,request,redirect,flash,url_for
import json
from validaçao.pp import LoginForm
from pathlib import Path
import os

app = Flask(__name__, template_folder = '../carros')
app.config['SECRET_KEY']="palavra_secreta123"

@app.route("/" , methods=["GET","POST"])
def login():
 
 form =LoginForm()
 return render_template("form.html" , form=form )
     
@app.route("/login", methods=["POST","GET"])
def route():
  
  usuario = request.form.get('nome')
  senha = request.form.get('senha')
  print(usuario)
  print(senha)
  with open('carros/usuarios.json') as usuarios:
    lista = json.load(usuarios)
  
    cont=0
    for c in lista:
      cont = 1
      if usuario == c['nome'] and senha == c['senha']:
        return render_template("lanchonete-lounge.html")
     
    else:
    
       flash('usuario ou senha incorreto')
       
    return redirect("/")

   
if __name__ in '__main__' : 
    app.run(debug=True)