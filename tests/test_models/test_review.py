#!/usr/bin/python3

"""Module that tests the review class
"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """TestReview Class
    """

    def test_create_review(self):
        """Test when  a review is created
        """

        my_model = Review()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Review')
