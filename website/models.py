from . import db
from flask_login import UserMixin


<<<<<<< HEAD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    foods = db.relationship('Food')

=======
class Restaurants(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(30))
    foods = db.relationship('Food')


<<<<<<< HEAD
class Organizations(db.Model):
=======
class Organizations(UserMixin, db.Model):
>>>>>>> tian
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(30))
>>>>>>> e20e89ec37ab91824b8f43c065a80025d5ccf56a


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(25))
    users_id = db.Column(db.Integer, db.ForeignKey('user.id'))
