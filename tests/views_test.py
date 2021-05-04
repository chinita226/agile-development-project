import unittest.mock
from website import views
from flask import Flask, render_template
from flask.ext.testing import TestCase
import unittest
from flask.ext.login import current_user
from flask import request
from base import BaseTestCase
from project.models import user

class views(BaseTestCase):

    # Ensure that the login page loads correctly
    def test_about(self):
        response = self.client.get('/about')
        self.assertIn(b'Please login', response.data)

class MyTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
    
    def test_about(self):
        self.app.get('/')
        self.assert_template_used('about.html')
    
    
class TestView(unittest.TestCase):

    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def test_home(self, mock_print):
        views.View.home(views)
        mock_print.assert_called_with("yummy saviour")
        
    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def test_dashboard(self, mock_print):
        views.View.dashboard(views)
        mock_print.assert_called_with("login")
        
    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def test_about(self, mock_print):
        views.View.about(views)
        mock_print.assert_called_with("NPO")
        