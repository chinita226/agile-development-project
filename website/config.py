"""Configuration objects for Flask app."""
class BaseSettings(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "s3cr3t"

class DevSettings(BaseSettings):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'
    DEBUG = True

class TestSettings(BaseSettings):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True