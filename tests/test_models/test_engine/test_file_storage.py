#!/usr/bin/python3
"""
test_file_storage module
"""
import models
import json
import os
import tempfile
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest import TestCase
from unittest.mock import patch, mock_open


class TestFileStorage(TestCase):
    """
    implementation of test for FileStorage class
    """

    def test_module_doc(self):
        """ Test for module documentation """
        doc_len = len(FileStorage.__module__.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_class_doc(self):
        """ Test for class documentation """
        doc_len = len(FileStorage.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_all_doc(self):
        """ Test for all() method documentation """
        doc_len = len(FileStorage.all.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_save_doc(self):
        """ Test for save() method documentation """
        doc_len = len(FileStorage.save.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_reload_doc(self):
        """ Test for reload() method documentation """
        doc_len = len(FileStorage.reload.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def setup(self):
        """ initialization """
        FileStorage.__file_path = "file.json"
        FileStorage.__objects = {}

    def test_all_method(self):
        """ Test for all() method """
        objs = FileStorage()
        test_objs = objs.all()
        self.assertIsInstance(test_objs, dict)

    def test_new_method(self):
        """ Test for new() method """
        obj = BaseModel()
        obj.name = "AirBnB"
        obj.my_number = 89
        file_storage = FileStorage()
        file_storage.new(obj)
        expected_key = f"{obj.__class__.__name__}.{obj.id}"
        objects = file_storage.all()
        self.assertIn(expected_key, objects)
        self.assertEqual(objects[expected_key], obj)

    def test_save_method(self):
        """ Test for save() method """
        test_objects = {
                'key1': {'id': 1, 'name': 'Object One'},
                'key2': {'id': 2, 'name': 'Object Two'}
                }

        file_storage = FileStorage()
        file_storage.__objects = test_objects
        file_storage.__file_path = 'file.json'
        save_inst = file_storage.save()
        self.assertFalse(save_inst)

        try:
            with tempfile.NamedTemporaryFile(
                    mode='w',
                    delete=False
                    ) as temp_file:
                json.dump(test_objects, temp_file)
                temp_file_path = temp_file.name

            with open(temp_file_path, 'r') as file:
                json_content = json.load(file)

            self.assertEqual(json_content, test_objects)
        finally:
            if temp_file_path:
                os.remove(temp_file_path)

    def test_reload_method(self):
        """ Test for reload() method """
        file_storage = FileStorage()
        file_storage.__file_path = 'test_file.json'
        reload_inst = file_storage.reload()
        self.assertFalse(reload_inst)


if __name__ == '__main__':
    unittest.main()
