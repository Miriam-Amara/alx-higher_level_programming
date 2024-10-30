#!/usr/bin/python3

"""
Unit tests for the Rectangle class.

This module tests the Rectangle class for correct initialization
and error handling.

Classes:
    TestRectangle: Contains tests for the Rectangle class.

Methods:
    setUp: Initializes test variables.
    test_valid_initialization: Validates correct Rectangle creation.
    test_value_error: Checks for ValueErrors with invalid parameters.
    test_type_error: Checks for TypeErrors with incorrect types.
"""

import unittest
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../models"))
)

from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Tests for the Rectangle class.
    """

    def setUp(self):
        """
        Initialize test variables.
        """
        self.a = 5
        self.b = 80
        self.c = -7
        self.d = 0
        self.list1 = [4, 5]
        self.tuple1 = (4, -4)
        self.set1 = {5, "j"}
        self.dict1 = {"name": "x", 1: 5}
        self.str1 = " "
        self.float1 = 4.50

    def test_valid_initialization(self):
        """
        Test valid Rectangle initialization.
        """
        obj = Rectangle(self.a, self.b)
        self.assertEqual(obj.width, self.a)
        self.assertEqual(obj.height, self.b)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

        obj1 = Rectangle(self.b, self.a, x=self.a, y=self.b, id=8)
        self.assertEqual(obj1.width, self.b)
        self.assertEqual(obj1.height, self.a)
        self.assertEqual(obj1.x, self.a)
        self.assertEqual(obj1.y, self.b)
        self.assertEqual(obj1.id, 8)

    def test_value_error(self):
        """
        Test ValueErrors for invalid parameters.
        """
        with self.assertRaises(ValueError):
            obj2 = Rectangle(self.c, self.a)
            print(obj2.width, "width")
        with self.assertRaises(ValueError):
            obj2 = Rectangle(self.a, self.d)

    def test_type_error(self):
        """
        Test TypeErrors for invalid types.
        """
        with self.assertRaises(TypeError):
            obj3 = Rectangle(self.list1, self.a)
        with self.assertRaises(TypeError):
            obj3 = Rectangle(self.a, self.b, self.a, self.set1)
        with self.assertRaises(TypeError):
            obj3 = Rectangle(self.tuple1, self.a)
        with self.assertRaises(TypeError):
            obj3 = Rectangle(self.a, self.dict1)
        with self.assertRaises(TypeError):
            obj3 = Rectangle(self.b, self.a, self.str1)
        with self.assertRaises(TypeError):
            obj3 = Rectangle(self.float1, self.a, self.str1)

if __name__ == "__main__":
    unittest.main()
