import os
from sqlalchemy import Column, String, Integer, create_engine, Date, Float
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import date


database_name = "castingagency"
database_path = 'postgres://vv@localhost:5432/' + database_name

db = SQLAlchemy()

'''
setup_db(app)
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.app = app
    db.init_app(app)
    db.create_all()
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    db_init_records()

# initilize some records in the table
def db_init_records():
    new_actor1 = (Actor(
        name = 'Andrew',
        gender = 'Male',
        age = 23
        ))
    new_actor2 = (Actor(
        name = 'Betty',
        gender = 'Female',
        age = 33
        ))
    new_movie1 = (Movie(
        title = 'Raiders of the lost Arc',
        release_date = date.today()
        ))
    new_movie2 = (Movie(
        title = 'Pursuit of happiness',
        release_date = date.today()
        ))

    new_actor1.insert()
    new_actor2.insert()

    new_movie1.insert()
    new_movie2.insert()

    db.session.commit()
'''
Movie
'''

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(db.DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


''''
Actor
'''

class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }