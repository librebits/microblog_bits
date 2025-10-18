from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fenix'}
    posts = [
        {
            'author': {'username': 'Juan'},
            'body': 'Bonito día en Antequera'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Tron - Ares, descargada via P2P !'
        }
    ]


    
    return render_template('index.html', title='Home', user=user, posts=posts)
