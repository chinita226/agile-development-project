from flask.globals import request
from website import db
from website.models import User
from flask_login import current_user
from werkzeug.security import generate_password_hash
from tests import BaseTestCase

class TestLogin(BaseTestCase):

    def setUp(self):
        with self.app.app_context() as context:
            self.context = context
            self.test_user = User(username='username',
                                  password=generate_password_hash('password', 'sha256'),
                                  businessname='business',
                                  location='Sweden',
                                  user_type='restaurant')
            self.context = context
            db.create_all()

            self.client = self.app.test_client()

    def tearDown(self):
        # clear the database at the end of the test
        with self.context:
            db.drop_all()
            db.session.remove()
            self.test_user = None


    def test_login(self):
        """Test GET /login."""
        response = self.client.get('/login')
        res = response.status_code
        exp = 200
        self.assertEqual(res, exp)


    def test_login_success(self):
        with self.context:
            with self.client as client:
                # Add test user to database
                db.session.add(self.test_user)
                db.session.commit()

                # Check current_user has no user object
                self.assertTrue(current_user == None)

                # Sign in with test users credentials
                response = client.post('/login',
                                       follow_redirects=True,
                                       data=dict(username=self.test_user.username,
                                                 password='password'))

                # Check the redirect url matches user dashboard url
                self.assertTrue(request.path == f'/{current_user.username}')
                # Check User object has been assigned to current_user
                self.assertTrue(current_user.username == self.test_user.username)
                # Check user is authenticated
                self.assertTrue(current_user.is_authenticated)


    def test_login_redirect(self):
        with self.context:
            with self.client as client:
                # Add test user to database
                db.session.add(self.test_user)
                db.session.commit()

                # Check current_user has no user object
                self.assertTrue(current_user == None)

                # Get login page when not authenticated
                response = client.get('/login', follow_redirects=True)

                # User is not logged in and should load login page CODE: 200
                self.assertTrue(response.status_code == 200)

                # Log the user in
                client.post('/login',
                            follow_redirects=True,
                            data=dict(username=self.test_user.username,
                                      password='password'))

                # Check user has been authenticated
                self.assertTrue(current_user.is_authenticated)

                # GET login page when authenticated
                response = client.get('/login', follow_redirects=False)

                # User is now logged in and should be redirected CODE: 302
                self.assertTrue(response.status_code == 302)


    def test_login_wrong_password(self):
        with self.context:
            with self.client as client:
                # Add test user to database
                db.session.add(self.test_user)
                db.session.commit()

                response = client.post('/login',
                                       follow_redirects=True,
                                       data=dict(username=self.test_user.username,
                                                 password='wrong'))

                # Check the error message is correct
                res = b'Incorrect username or password!' in response.data
                self.assertTrue(res)


    def test_login_wrong_username(self):
        with self.context:
            with self.client as client:
                # Add test user to database
                db.session.add(self.test_user)
                db.session.commit()

                response = client.post('/login',
                                       follow_redirects=True,
                                       data=dict(username='wrong',
                                                 password='password'))

                # Check the error message is correct
                res = b'Incorrect username or password!' in response.data
                self.assertTrue(res)


    def test_logout(self):
        with self.context:
            with self.client as client:
                db.session.add(self.test_user)
                db.session.commit()

                client.post('/login',
                            follow_redirects=True,
                            data=dict(
                                username=self.test_user.username,
                                password='password'
                            ))

                self.assertTrue(current_user.is_authenticated)

                response = client.post('/logout', follow_redirects=True)

                self.assertTrue(not current_user.is_authenticated)

                res = request.path
                exp = '/login'
                self.assertEqual(res, exp)

                msg = b'Log out successful!'
                self.assertTrue(msg in response.data)