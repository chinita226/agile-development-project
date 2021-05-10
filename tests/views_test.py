import unittest
from tests import BaseTestCase
from website.models import Food, User
from flask_login import current_user
from flask import request, Response
from werkzeug.security import generate_password_hash
from website import db

class TestFunctions(BaseTestCase):

    ### TEST INITIALIZATION AND TEAR DOWN ###

    def setUp(self):
        with self.app.app_context() as context:
            self.context = context
            self.test_user = User(username='username',
                                    password=generate_password_hash('password', 'sha256'),
                                    businessname='testbusiness',
                                    location='Sweden',
                                    user_type='restaurant')
            
            self.test_food = Food(food_name='the name',
                                    description='dec',
                                    quantity='num of items',
                                    users_id='id')
            self.context = context
            db.create_all()

            self.client = self.app.test_client()


    def tearDown(self):
        # clear the database at the end of the test
        with self.context:
            db.drop_all()
            db.session.remove()
            self.test_user = None

    def test_delete(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.add(self.test_food)
            db.session.commit()
            with self.client as client:

                food = db.session.query(Food.id).filter_by(food_name='the name').first()
                self.assertTrue(food)

                client.post(
                    '/login',
                    follow_redirects=True,
                    data=dict(
                        username=self.test_user.username,
                        password='password'
                    )
                )
                self.assertTrue(current_user.is_authenticated)

                response = client.post(
                    '/delete',
                    follow_redirects=True,
                    data=dict(
                        id=food.id
                    )
                )
                the_food = Food.query.filter_by(id=food.id).count()
                self.assertTrue(the_food == 0)

    def test_add(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.add(self.test_food)
            db.session.commit()
            with self.client as client:

                food = db.session.query(Food.id).filter_by(food_name='the name', description='something', quantity='5').populate_existing()
                self.assertTrue(food)

                client.post(
                    '/login',
                    follow_redirects=True,
                    data=dict(
                        username=self.test_user.username,
                        password='password'
                    )
                )
                self.assertTrue(current_user.is_authenticated)

                response = client.post(
                    '/<user>',
                    follow_redirects=True,
                    data=dict(
                        food_name='the name',
                        description='something',
                        quantity='5')
                )

                the_food = Food.query.filter_by(id=food.id).count()
                self.assertTrue(the_food == 1)


    # def test_update(self):
    #     with self.context:
    #         db.session.add(self.test_user)
    #         db.session.add(self.test_food)
    #         db.session.commit()
    #         with self.client as client:

    #             food = db.session.query(Food.id).filter_by(food_name='the name').first()
    #             self.assertTrue(food)

    #             client.post(
    #                 '/login',
    #                 follow_redirects=True,
    #                 data=dict(
    #                     username=self.test_user.username,
    #                     password='password'
    #                 )
    #             )
    #             self.assertTrue(current_user.is_authenticated)

    #             response = client.post(
    #                 '/update',
    #                 follow_redirects=True,
    #                 data=dict(newname='newname',
    #                           oldname='oldname',
    #                           newdes='newdes',
    #                           olddes='olddes',
    #                           olduantity='oldquantity',
    #                           newquantity='newquantity')

    #             )
    #             food = Food.query.filter_by(food_name=oldname, description=olddes, quantity=oldquantity ).first()
    #             self.assertTrue(food == 1)


class TestViews(BaseTestCase):

    def test_home(self):

        with self.app.test_client() as client:

            response = client.get('/')

            self.assertTrue(response.status_code == 200)
