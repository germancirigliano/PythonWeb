import os
from dotenv import load_dotenv
load_dotenv()
page_name = os.environ.get('NAME')

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    props = {
        "name": f'{page_name}'
    }
    return render_template('home.html', props=props)

@app.route("/registro")
def register():
    props = {
        "name": f'Registro - {page_name}'
    }
    return render_template('register.html', props=props)

@app.route("/iniciar-sesion")
def login():
    props = {
        "name": f'Iniciar Sesion - {page_name}'
    }
    return render_template('login.html', props=props)