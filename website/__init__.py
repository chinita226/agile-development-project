from flask import Flask


def create_web():
    web = Flask(__name__)
    web.config['SECRET_KEY'] = 'whhhhhaaatteeverr'

    from website.auth import auth
    from website.views import views

    web.register_blueprint(auth, url_prefix='/')
    web.register_blueprint(views, url_prefix='/')

    return web
