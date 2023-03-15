#!/usr/bin/python3

"""Module that tests the user class
"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """TestUser Class
    """

    def test_create_user(self):
        """Test when a user is created
        """

        my_model = User()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'User')
