#!/usr/bin/python3
"""
Module of test FileStorage
"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import os


class TestFileStorage(unittest.TestCase):
    '''
    Test cases for file_storage class
    '''

    def setUp(self):
        '''
        simple set up
        '''
        self.my_model = BaseModel()
        self.storage = FileStorage()

    def test_new(self):
        '''
        tests new method in file storage
        '''
        self.storage.new(self.my_model)
        new_dict = self.storage.all()
        key = self.my_model.__class__.__name__ + '.' + self.my_model.id
        self.assertIsInstance(new_dict[key], BaseModel)

    def test_all(self):
        '''
        tests if all returns a dict
        '''
        self.assertIsInstance(self.storage.all(), dict)

    def test_save(self):
        '''
        tests the save method of file storage class
        '''
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_json_file_content_type(self):
        '''
        tests if the content of the json file is type of dict
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding='utf-8') as fd:
            data = json.load(fd)

        self.assertIsInstance(data, dict)


if __name__ == "__main__":
    unittest.main()
