from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = 'test.db'
DB_NAME2 = 'food.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'whhhhhaaatteeverr'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME2}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

    from .models import User
    from .models import Food

    create_table(app)

    return app

def create_table(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
        
def create_table(app):
    if not path.exists('website/' + DB_NAME2):
        db.create_all(app=app)
        print('Created Database!')

