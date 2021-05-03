from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from os import path

db = SQLAlchemy()
DB_NAME = 'test.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'whhhhhaaatteeverr'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import Restaurants

    @login_manager.user_loader
    def load_restaurant(id):
        return Restaurants.query.get(int(id))

    from .models import Organizations

    @login_manager.user_loader
    def load_organization(id):
        return Organizations.query.get(int(id))

    from website.auth import auth
    from website.views import views

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    from .models import User

    create_table(app)

<<<<<<< HEAD
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
=======
>>>>>>> e20e89ec37ab91824b8f43c065a80025d5ccf56a
    return app

def create_table(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

