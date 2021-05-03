from . import db
from flask_login import UserMixin


class Restaurants(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(30))
    foods = db.relationship('Food')


class Organizations(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(30))


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(25))
    restaurants_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
