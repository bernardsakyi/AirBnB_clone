#!/usr/bin/python3

"""Module that tests the place class
"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestPlace Class
    """

    def test_create_place(self):
        """Test when  a place is created
        """

        my_model = Place()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Place')
