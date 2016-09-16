from src import app
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from src.models import db, Practice, add_session
from config import SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = SECRET_KEY

# first time init, run this in terminal
# to create the DB
# >>> import src
# >>> src.models.db.create_all(app=src.app)

db.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('base.html')

    if request.method == 'POST':
        add_session(db, request.form)
        return render_template('base.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/refresh', methods=['POST', 'GET'])
def refresh():
    if request.method == 'GET':
        return redirect(url_for('/'))

    if request.method == 'POST':
        # do the refresh
        return redirect(url_for('/'))


@app.route('/edit')
def edit():
    return render_template('base.html')

@app.route('/check')
def check():
    print(Practice.query.all())
    return render_template('base.html')
