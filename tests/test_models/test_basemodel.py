#!/usr/bin/env python3

"""Test Base Model"""
from datetime import datetime
import unittest
import inspect
import models
from models.base_model import BaseModel
from unittest import mock
from unittest.mock import MagicMock


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class
    """

    def test_cases(self):
        """tests the principals cases
        """

        my_model = BaseModel()
        ids = uuid.UUID(my_model.id)
        self.assertIsInstance(ids, uuid.UUID)
        self.assertIsInstance(my_model.created_at, datetime)
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Check pep8")

    def test_create_base_model(self):
        """Test when a base_model is created
        """

        my_model = BaseModel()
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_save(self):
        """Test when saves the model
        """

        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        """Test when adds the new attributes to the list
        """

        my_model = BaseModel()
        result = my_model.to_dict()
        self.assertEqual(result['__class__'], 'BaseModel')
