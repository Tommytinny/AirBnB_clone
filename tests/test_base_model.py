#!/usr/bin/python3
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel_instantiation(unittest.TestCase):
    '''Testing for the instantiation of the basemodel'''
    def test_instantiation(self):
        '''Test instantiations'''
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_instantiation_with_kwargs(self):
        """Test instantiation with keyword arguments"""
	kwargs = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-01T00:00:00.000000'
        }
        model = BaseModel(**kwargs)
	for key, value in kwargs.items():
            self.assertEqual(getattr(model, key), value if key not in 
            ['created_at', 'updated_at']
            else datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))

    def test_str_method(self):
        """Test the string representation"""
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model.__str__(), expected_str)

    def test_save_method(self):
        """Test the save method updates 'updated_at'"""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)
        self.assertTrue(model.updated_at > original_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method functionality"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('create_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()