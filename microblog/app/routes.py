from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'beautiful day in the Philippines!'
        },
        {
            'author': {'username': 'Juliana'},
            'body': 'saw a cute cat today!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)