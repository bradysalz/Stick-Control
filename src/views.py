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
        return render_template('home.html')

    if request.method == 'POST':
        add_session(db, request.form)
        return render_template('home.html')


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


@app.route('/data/<exercise_name>')
def show_data(exercise_name):
    dataset = Practice.query.all()
    return render_template('data.html', dataset=dataset)


@app.route('/edit')
def edit():
    return render_template('base.html')


@app.route('/check')
def check():
    data = Practice.query.all()
    data = [(d.date, d.number, d.tempo) for d in data]
    date, number, tempo = zip(*data)
    
    date = [d.strftime("%m/%d/%Y") for d in date]
    
    header = "Date,Number,Tempo\n"
    body = [date[n] + ',' + str(number[n]) + ',' + str(tempo[n])
            for n in range(len(date))]
    body = '\n'.join(body)
    return render_template('home.html', data=header+body)
