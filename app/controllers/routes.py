from flask import render_template
from app import app

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/sobre/')
@app.route('/about/')
def about():
    return render_template('sobre.html')
