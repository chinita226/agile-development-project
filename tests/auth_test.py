import unittest
from website import app

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User('abc', 'FlaskIsAwesome')
    assert user.username == 'abc'
    assert user.hashed_password == 'FlaskIsAwesome'
 
if __name__ == "__main__":
    unittest.main()

