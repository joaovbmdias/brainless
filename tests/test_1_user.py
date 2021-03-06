import sys
import os
os.chdir('src/')
sys.path.append(os.getcwd())

if os.path.exists(os.getcwd()+'/brainless.db'):
    os.remove(os.getcwd()+'/brainless.db')

import unittest
from configuration import db
from models.user import User
import constants

db.metadata.create_all(db.engine)
unittest.TestLoader.sortTestMethodsUsing = None

class TestUser(unittest.TestCase):
    """
    Unit Testing User
    """
    def test_1_1_create(self):
        """
        Test that it can create a user
        """
        user = User(username   = "test_username",
                    password   = "test_password",
                    first_name = "test_first_name",
                    last_name  = "test_last_name")

        result = user.create()

        self.assertIsNotNone(user.id, "User ID cannot be None")
        self.assertGreater(user.id, 0, "User ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_2_1_create_same(self):
        """
        Test that it cannot create an already existing user
        """
        user = User(username   = "test_username",
                    password   = "test_password",
                    first_name = "test_first_name",
                    last_name  = "test_last_name")        
        
        result = user.create()

        self.assertIsNone(user.id, "User ID must be None")
        self.assertEqual(result, constants.FAILURE)

if __name__ == '__main__':
    db.metadata.create_all(db.engine)
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
