from . import db
from flask_login import UserMixin
<<<<<<< HEAD
 
 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), unique=True, nullable=False)
=======


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
>>>>>>> 741512dbe7ca26d0197c05a8612fabf3541b2cf4
    password = db.Column(db.String(30), nullable=False)
    user_type = db.Column(db.String(30), nullable=False)
    foods = db.relationship('Food')
<<<<<<< HEAD
 
 
=======


>>>>>>> 741512dbe7ca26d0197c05a8612fabf3541b2cf4
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(25))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
