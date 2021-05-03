from flask_testing import TestCase
import requests
from website import __init__, db
import flask_unittest
    
class BaseTestCase(TestCase):
    def create_app(self):
        return create_app('test')

