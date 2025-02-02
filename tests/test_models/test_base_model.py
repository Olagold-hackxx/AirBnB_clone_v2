#!/usr/bin/python3
"""H"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """H"""

    def __init__(self, *args, **kwargs):
        """base_model"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """base_model"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """base_model"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs_int(self):
        """base_model"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """base_model"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.to_dict()))

    def test_todict(self):
        """base_model"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """base_model"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """base_model"""
        n = {'Name': 'test'}
        try:
            with self.assertRaises(KeyError):
                new = self.value(**n)
        except Exception:
            pass

    def test_id(self):
        """base_model"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """base_model"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """base_model"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()


if __name__ == '__main__':
    unittest.main()
