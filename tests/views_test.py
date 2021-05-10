""""""
from tests import BaseTestCase
from website import db
from website.models import User

class TestViews(BaseTestCase):

    def test_home(self):

        with self.app.test_client() as client:

            response = client.get('/')

            self.assertTrue(response.status_code == 200)