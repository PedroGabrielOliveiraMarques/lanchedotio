from flask import Flask, render_template,request,redirect,flash,url_for
import json
from nome.pp import LoginForm
from pathlib import Path
import os


app = Flask(__name__, template_folder = '../carros')
app.config['SECRET_KEY']="palavra_secreta123"

@app.route("/" , methods=["GET","POST"])
def login():

      return("O ITEM NAO FOI CONECTADO")
 
if __name__ == "__main__" : 
    app.run(debug=True)