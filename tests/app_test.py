from typing import ByteString
import unittest
from website import create_app, create_test_app
from flask import Flask

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()


    def test_create_app(self):
        self.assertIsInstance(self.app, Flask)


    def test_create_app_config(self):
        app = self.app
        database = app.config['SQLALCHEMY_DATABASE_URI']
        env = app.config['FLASK_ENV']
        secret = app.config['SECRET_KEY']
        debug = app.config['DEBUG']
        track = app.config['SQLALCHEMY_TRACK_MODIFICATIONS']

        self.assertEqual(database, 'sqlite:///sqlite.db')
        self.assertEqual(env, 'development')
        self.assertEqual(secret, 's3cr3t')
        self.assertTrue(debug)
        self.assertFalse(track)