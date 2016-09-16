from src import app
from flask import request, render_template, send_file, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from src.models import db
from config import SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = SECRET_KEY

# first time init, run this in terminal
# to create the DB
# >>> import src
# >>> src.models.db.create_all(app=src.app)

db.init_app(app)

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/add')
def add_practice():
    return render_template('add.html')

@app.route('/refresh', methods=['POST', 'GET'])
def refresh():
    if request.method == 'GET':
        return redirect(url_for('/')) 

    if request.method == 'POST':
        # do the refresh
        return redirect(url_for('/'))         