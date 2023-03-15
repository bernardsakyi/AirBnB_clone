#!/usr/bin/python3

"""Module that tests the city class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """TestCity Class
    """

    def test_create_city(self):
        """Test when  a city is created
        """

        my_model = City()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'City')
