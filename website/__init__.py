from flask import Flask


def create_web():
    web = Flask(__name__)
    web.config['SECRET_KEY'] = 'whhhhhaaatteeverr'

    from website.auth import auth

    web.register_blueprint(auth, url_prefix='/')

    return web
