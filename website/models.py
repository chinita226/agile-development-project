
from . import db


class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(30))
    foods = db.relationship('Food')

class Orgazations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(30))

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(25))
    restaurants_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
