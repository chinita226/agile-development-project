import unittest
from tests import BaseTestCase
from website.models import User
from flask_login import current_user
from flask import request
from werkzeug.security import generate_password_hash
from website import db

class TestSignup(BaseTestCase):

    ### TEST INITIALIZATION AND TEAR DOWN ###

    def setUp(self):
        with self.app.app_context() as context:
            self.context = context
            self.test_user = User(username='username',
                                    password=generate_password_hash('password', 'sha256'),
                                    businessname='testbusiness',
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


    ### TESTS ###


    def test_signup(self):
        """Test GET /signup."""
        response = self.client.get('/signup')
        res = response.status_code
        exp = 200
        self.assertEqual(res, exp)


    def test_signup_redirect(self):
        """Test GET signup redirects logged in user to dashboard"""
        with self.context:
            with self.client as client:
                # Add test user to database
                db.session.add(self.test_user)
                db.session.commit()

                # Check current_user has no user object
                self.assertTrue(current_user == None)

                # Log the user in
                client.post('/login',
                                    follow_redirects=True,
                                    data=dict(username=self.test_user.username,
                                                password='password'))

                # Check user has been authenticated
                self.assertTrue(current_user.is_authenticated)

            with self.client as client:
                # GET login page when authenticated
                response = client.get('/signup', follow_redirects=True)

                # User is now logged in and should be redirected to dashboard url
                res = request.path
                exp = f'/{self.test_user.username}'
                self.assertTrue(response.status_code == 200)


    def test_user_registered_as_current_user_on_signup(self):
        """Test user can register"""
        with self.context:
            with self.client as client:
                # Check there is no current_user object
                self.assertTrue(current_user == None)

                # Execute the post request
                response = client.post('/signup',
                                    data=dict(username='test',
                                                password='password',
                                                confirm='password',
                                                businessname='testname',
                                                location='sweden',
                                                user_type='restaurant'
                                                ), follow_redirects=True)

                # Check user object has been assigned to current_user
                self.assertTrue(current_user.username == 'test')


    def test_user_added_to_database_on_signup(self):
        """Test user added to database when registering."""
        with self.context:
            # Search database for user by username
            user = User.query.filter_by(username='test').first()

            # Check user is None
            self.assertTrue(user == None)

            # Execute the signup request
            response = self.client.post('/signup',
                                data=dict(username='test',
                                            password='password',
                                            confirm='password',
                                            businessname='testname',
                                            location='sweden',
                                            user_type='restaurant'
                                            ), follow_redirects=True)

            # Query Database after user registers
            user = User.query.filter_by(username='test').first()

            # Check that user has been instantiated.
            self.assertIsInstance(user, User)

    def test_user_values_set_on_signup(self):
        """User values set in database on register."""
        with self.context:
            response = self.client.post('/signup',
                                   data=dict(username='test',
                                             password='password',
                                             confirm='password',
                                             businessname='testname',
                                             location='sweden',
                                             user_type='npo'
                                             ), follow_redirects=True)
            # Retrieve user from database
            user = User.query.filter_by(username='test').first()

            # Check users values
            self.assertEqual(user.username, 'test')
            self.assertEqual(user.user_type, 'npo')

            # Check password has been hashed
            self.assertNotEqual(user.password, 'password')


    def test_signup_missing_form_field(self):
        with self.client as client:
            response = self.client.post('/signup',
                                        data=dict(username='test',
                                                  password='password',
                                                  confirm='password',
                                                  location='sweden',
                                                  user_type='restaurant'
                                                  ), follow_redirects=True)

            self.assertTrue(b"Missing required fields" in response.data)


    def test_signup_with_existing_username(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.commit()
            with self.client as client:
                response = client.post('/signup',
                                       data=dict(username=self.test_user.username,
                                                 password='password',
                                                 confirm='password',
                                                 businessname='testname',
                                                 location='sweden',
                                                 user_type='restaurant'
                                                 ), follow_redirects=True)

                self.assertTrue(b'Username not available!' in response.data)


    def test_signup_with_existing_business_name(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.commit()
            with self.client as client:
                response = client.post('/signup',
                                       data=dict(username='name',
                                                 password='password',
                                                 confirm='password',
                                                 businessname=self.test_user.businessname,
                                                 location='sweden',
                                                 user_type='restaurant'
                                                 ), follow_redirects=True)

                self.assertTrue(b'Business name is already in use!' in response.data)


    def test_signup_with_wrong_passwords(self):
        with self.client as client:
            response = client.post('/signup',
                                    data=dict(username='name',
                                                password='password',
                                                confirm='wrong',
                                                businessname=self.test_user.businessname,
                                                location='sweden',
                                                user_type='restaurant'
                                                ), follow_redirects=True)

            self.assertTrue(b'The passwords do not match!' in response.data)