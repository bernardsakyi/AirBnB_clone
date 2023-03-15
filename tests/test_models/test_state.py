#!/usr/bin/python3

"""Module that tests the state class
"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """TestState Class
    """

    def test_create_state(self):
        """Test when a state is created
        """

        my_model = State()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'State')
