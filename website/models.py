from . import db
from flask_login import UserMixin


<<<<<<< HEAD
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    user_type = db.Column(db.String(30), nullable=False)
=======
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
>>>>>>> main
    foods = db.relationship('Food')


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(25))
<<<<<<< HEAD
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
=======
    users_id = db.Column(db.Integer, db.ForeignKey('user.id'))
>>>>>>> main
