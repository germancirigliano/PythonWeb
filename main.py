import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask import render_template

app = Flask(
    __name__,
    static_url_path='', 
    static_folder='web/static',
    template_folder='web/templates'
)

page_name = os.environ.get('NAME')
company_name = os.environ.get('NAME')
base_props = {
        "company": f'{page_name}',
        "year": datetime.now().year
}

@app.route("/")
def home():
    props = {
        "name": f'{page_name}'
    }
    props.update(base_props)
    return render_template('pages/home.html', props=props)

@app.route("/registro")
def register():
    props = {
        "name": f'Registro - {page_name}'
    }
    props.update(base_props)
    return render_template('pages/register.html', props=props)

@app.route("/iniciar-sesion")
def login():
    props = {
        "name": f'Iniciar Sesion - {page_name}'
    }
    props.update(base_props)
    return render_template('pages/login.html', props=props)