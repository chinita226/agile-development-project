from flask.globals import request
from website import db
from website.models import User, Food
from flask_login import current_user
from werkzeug.security import generate_password_hash
from tests import BaseTestCase

class TestViews(BaseTestCase):

    def setUp(self):
        """Initialise the test."""
        with self.app.app_context() as context:
            self.context = context
            self.test_user = User(
                id=1,
                username='username',
                password=generate_password_hash('password', 'sha256'),
                businessname='business',
                location='Sweden',
                user_type='restaurant'
            )

            self.test_food = Food(
                id=1,
                food_name = 'the name',
                description = 'the description',
                quantity = 10,
                users_id = 1
            )

            self.context = context
            db.create_all()

            self.client = self.app.test_client()

    def tearDown(self):
        """Clean up after the test."""
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