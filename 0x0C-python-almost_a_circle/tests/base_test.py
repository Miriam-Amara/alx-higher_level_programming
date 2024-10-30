#!/usr/bin/python3

"""
base_test module

This module provides BaseTest class, which serves as
unittest for base module
"""


import unittest
import sys
import os


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../models"))
)

from base import Base


class BaseTest(unittest.TestCase):
    """
    A class used for testing the base class.
    """

    def setUp(self):
        pass

    def test_init_method(self):
        """
        Test Base initialization with specific and default ids.
        """
        input_ids = [3, 0, None, 12]
        expected_ids = [1, 3, 2, 0, 3, 4, 5, 12]
        input_index = 0

        for i in range(8):
            if i % 2:
                # use id from input_ids
                b = Base(id=input_ids[input_index])
                self.assertEqual(b.id, expected_ids[i])
                input_index += 1
            else:
                # default id (auto-increment)
                b = Base()
                self.assertEqual(b.id, expected_ids[i])


if __name__ == "__main__":
    unittest.main()
