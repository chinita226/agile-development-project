import unittest
import unittest.mock
from website import auth, create_app


class TestAuth(unittest.TestCase):

    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def test_login(self, mock_print):
        auth.Auth.login(auth)
        mock_print.assert_called_with("test")

    app = create_app()

    def test_auth_create_user(self):
        tester = self.app.test_client(self)
        response = tester.get('/signup')
        self.assertEqual(response.status_code, 200)

        response = tester.post('/signup', data={'username': 'a'})
        self.assertEqual(response.status_code, 500)
        response = tester.post(
            '/signup', data={'username': "osagieosahenagharu@1234", 'password': "osagieosahenagharu@1234"})
        self.assertEqual(response.status_code, 302)
        response = tester.post('/signup',
                               data={'username': "osagieosahenagharu", 'password': "osagieosahenagharu@1234", 'confirm': "osagieosahenagharu@1234"})
        self.assertEqual(response.status_code, 302)

        response = tester.post('/signup',
                               data={'username': "osagieosahenagharu",
                                     'password': "osagieosahenagharu@1234",
                                     'confirm': "osagieosahenagharu@1234",
                                     "org_type": "testing"})
        self.assertEqual(response.status_code, 302)

    def test_auth_login(self):
        tester = self.app.test_client(self)
        response = tester.get('/login')
        self.assertEqual(response.status_code, 200)
        response = tester.post('/login', data={'username': 'a'})
        self.assertEqual(response.status_code, 302)
        response = tester.post('/login', data={'username': "a", 'password': "a"})
        self.assertEqual(response.status_code, 302)
        response = tester.post('/login', data={'username': "osagieosahenagharu", 'password': "osagieosahenagharu@1234"})
        self.assertEqual(response.status_code, 302)

    def test_auth_logout(self):
        tester = self.app.test_client(self)
        response = tester.get('/logout')
        self.assertEqual(response.status_code, 302)
