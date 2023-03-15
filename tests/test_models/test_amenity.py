#!/usr/bin/python3

"""Module that tests the amenity class
"""

import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from models.base_model import BaseModel
from unittest.mock import patch
import pycodestyle
import models


class TestAmenity(unittest.TestCase):
    """TestAmenity Class
    """

    def test_create_amenity(self):
        """Test when  a amenity is created
        """

        my_model = Amenity()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Amenity')
