from re import search
from tests.base_test import BaseTestCase
from website.models import Food, User
from flask_login import current_user
from werkzeug.security import generate_password_hash
from website import db


class TestViewRoutes(BaseTestCase):

    # TEST INITIALIZATION AND TEAR DOWN #

    def setUp(self):
        with self.app.app_context() as context:
            self.context = context
            self.client = self.app.test_client()

            self.test_user = User(username='username',
                                  password=generate_password_hash('password', 'sha256'),
                                  businessname='testbusiness',
                                  location='Sweden',
                                  user_type='restaurant')

            self.test_food = Food(id=1,
                                  food_name='name',
                                  description='desc',
                                  quantity='qty',
                                  users_id=self.test_user.id)

            db.create_all()

    def tearDown(self):
        # clear the database at the end of the test
        with self.context:
            db.drop_all()
            db.session.remove()
            self.test_user = None

    def test_home(self):

        with self.app.test_client() as client:

            response = client.get('/')

            self.assertTrue(response.status_code == 200)

    def test_delete(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.add(self.test_food)
            db.session.commit()
            with self.client as client:

                food = db.session.query(Food.id).filter_by(food_name='name').first()
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

                client.post(
                    '/delete',
                    follow_redirects=True,
                    data=dict(
                        id=food.id
                    )
                )

                the_food = Food.query.filter_by(id=food.id).count()
                self.assertTrue(the_food == 0)

    def test_add_food(self):
        """User can add a food object to the database."""
        with self.context:
            db.session.add(self.test_user)
            db.session.commit()
            with self.client as client:
                client.post(
                    '/login',
                    follow_redirects=True,
                    data=dict(
                        username=self.test_user.username,
                        password='password'
                    )
                )

                self.assertTrue(current_user.is_authenticated)

            with self.client as client:

                food = self.test_food

                client.post(
                    '/add-food',
                    follow_redirects=True,
                    data=dict(
                        id=food.id,
                        food_name=food.food_name,
                        description=food.description,
                        quantity=food.quantity)
                )

                the_food = Food.query.filter_by(id=food.id).first()
                self.assertTrue(the_food)

                # Values of food object returned from database
                res = [
                    the_food.id,
                    the_food.food_name,
                    the_food.description,
                    the_food.quantity,
                    the_food.users_id
                    ]
                # Class food objects values
                exp = [
                    food.id,
                    food.food_name,
                    food.description,
                    food.quantity,
                    current_user.id
                    ]

                self.assertEqual(res, exp)

    def test_delete_flash_message(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.add(self.test_food)
            db.session.commit()
            with self.client as client:

                food = db.session.query(Food.id).filter_by(food_name='name').first()
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

                client.post(
                    '/delete',
                    follow_redirects=True,
                    data=dict(food_name='name',
                              description='cheese',
                              quantity='2',
                              id='1')
                )

                msg = b'Item Deleted!'
                self.assertTrue(msg)

    def test_add_food_flash_message(self):
        """User can add a food object to the database."""
        with self.context:
            db.session.add(self.test_user)
            db.session.commit()
            with self.client as client:
                client.post(
                    '/login',
                    follow_redirects=True,
                    data=dict(
                        username=self.test_user.username,
                        password='password'
                    )
                )

                self.assertTrue(current_user.is_authenticated)

            with self.client as client:

                food = self.test_food

                client.post(
                    '/add-food',
                    follow_redirects=True,
                    data=dict(
                        id=food.id
                    )
                )
                the_food = Food.query.filter_by(id=food.id).first()
                self.assertTrue(the_food)

                msg = b'Item Added!'
                self.assertTrue(msg)

    def test_update_flash_message(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.add(self.test_food)
            db.session.commit()
            with self.client as client:
                client.post(
                    '/login',
                    follow_redirects=True,
                    data=dict(
                        username=self.test_user.username,
                        password='password'
                    )
                )

                self.assertTrue(current_user.is_authenticated)

                food = self.test_food

                self.assertTrue(food.food_name == 'name')

                client.post(
                    '/update/<id>',
                    follow_redirects=True,
                    data=dict(
                        id=food.id,
                        name='updated',
                        description='updated',
                        quantity=200)
                )

                updated = Food.query.filter_by(id=food.id).first()
                self.assertTrue(food)

                res = [
                    updated.food_name,
                    updated.description,
                    updated.quantity
                ]

                exp = [
                    'updated',
                    'updated',
                    200
                ]

                self.assertEqual(res, exp)

                msg = b'Item Updated!'
                self.assertTrue(msg)

    def test_blog(self):
        with self.client as client:
            res = client.get('/food-waste')

            self.assertTrue(res.status_code == 200)

    def test_npo_search_no_tag(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.add(self.test_food)
            db.session.commit()
            with self.client as client:
                client.post(
                    '/login',
                    follow_redirects=True,
                    data=dict(
                        username=self.test_user.username,
                        password='password'
                    )
                )
                self.assertTrue(current_user.is_authenticated)

                # If we assign the post to a variable like below. We will get the response
                # object as the value. Then you can check properties of the response object
                # like status_code or data etc.

                response = client.post(
                    '/search',
                    follow_redirects=True,
                    # The values in the dict() should correspond to any values
                    # you use in the form. So for this route, it is just the
                    # tag.
                    # The way you were doing the post to the route, just returned
                    # a 400 status error for 'Bad request' because you were passing
                    # form values that didn't exist.
                    data=dict(
                        tag=''
                        # No tag value passed in above by providing an empty string as value.
                        # The "if not tag:" code block in the search function of views.py
                        # will run. So we can check if the correct flash message was
                        # inserted into the html template.
                        )
                )

                # Here we will check the flash message by checking if the message
                # is in the response data. The response data is a bytes object,
                # so you need to prefix the string with b. Like below:
                self.assertTrue(b'Missing keyword' in response.data)
                # response.data returns the html for the page it will route to.
                # I have added a print statement to show you. If you run the tests
                # with `make coverage` command from the terminal. It will print the
                # data when the test runs.
                print(response.data) # This is just to show you what the response.data is

    def test_npo_search_invalid_search_term(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.commit()
            with self.client as client:
                client.post(
                    '/login',
                    follow_redirects=True,
                    data=dict(
                        username=self.test_user.username,
                        password='password'
                    )
                )

                self.assertTrue(current_user.is_authenticated)

            with self.client as client:

                user = self.test_user

                # Set this post value to a variable like i did in the previous test.
                # That way you can check the properties of the response object.
                # Like below:
                # response = client.post( ### Your parameters go here ### )

                client.post(
                    '/search',
                    follow_redirects=True,
                    data=dict(
                        # Here you should be have provided a value for tag,
                        # not location because tag is what is in the form.
                        # So you just pass a value to tag, that isn't an empty
                        # string like the previous test but it also isnt a
                        # correct location.
                        # For our tests, at the very top of this
                        # file, we have a set up function. In there we have a
                        # test user. The test users location is "Sweden". There is
                        # also a test_food and the users_id for the test_food
                        # is the id of the test user. So the location value for the food
                        # will correspond to that of the test_user. So any value
                        # other than "Sweden" will be an invalid location.
                        # So you could have something like below:
                        # tag='Vietnam'

                        location="None" # You can remove this and replace it with tag.
                    )
                )

                # You don't need to check anything with the user so you don't need
                # the line below.
                the_user = User.query.filter_by(location=user.location).first()

                # You want to check for the message. So you can do that by checking response.data
                # like i did in the previous test.

    def test_npo_search_valid_location(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.add(self.test_food)
            db.session.commit()
            with self.client as client:

    def test_npo_search_valid_businessname(self):
        with self.context:
            db.session.add(self.test_user)
            db.session.add(self.test_food)
            db.session.commit()
            with self.client as client:


