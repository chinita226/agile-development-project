from flask import Flask
from website.config import DevSettings, TestSettings
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,  login_manager
from os import path

db = SQLAlchemy()
DB_NAME = 'test.db'

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevSettings)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    from .models import Food

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from website.auth import auth
    from website.views import views

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    create_table(app)

    return app


def create_table(app):
    if not path.exists('website/' + DevSettings.SQLALCHEMY_DATABASE_URI):
        db.create_all(app=app)
        print('Created Database!')
