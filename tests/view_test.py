import unittest

from website import create_app


class TestView(unittest.TestCase):
    app = create_app()

    def test_view_home_page(self):
        tester = self.app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 302)

    def test_view_about_page(self):
        tester = self.app.test_client(self)
        response = tester.get('/about')
        self.assertEqual(response.status_code, 200)
