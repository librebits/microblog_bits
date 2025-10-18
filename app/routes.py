from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fenix'}
    return '''
    <html>
        <head>
            <title>Home Page ~  Microblog</title>
        </head>

        <body>
        </body>

    
    
    </html>
    '''
