from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Practice(db.Model):
    """One practice item."""

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String(128)) # session name
    number = db.Column(db.Integer)   # lesson number
    tempo = db.Column(db.Integer)    # tempo

    def __init__(self, date=0, name=0, number=0, tempo=0):
        if date == 0:
            self.date = datetime.datetime.utcnow()
        else:
            self.date = date

        self.name = name
        self.number = number
        self.tempo = tempo


    def __repr__(self): 
        return "<Practice Lesson {0} at {1} bpm on {2}".format(
            self.number, 
            self.tempo, 
            self.date)

def add_session(db, form):
    """Add practice sesion to the database."""
    exercise = form['exercise-name']
    start = int(form['exercise-start'])
    stop = int(form['exercise-stop'])
    tempo = int(form['tempo'])
    date = datetime.strptime(form['practice-date'], '%m/%d/%y')

    for e in range(start, stop):
        prac = Practice(date, exercise, e, tempo)
        db.session.add(prac)

    db.session.commit()


