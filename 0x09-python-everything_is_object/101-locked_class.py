#!/usr/bin/python3

"""
101-locked_class.py

This module provides the LockedClass class for preventing users
from dynamically creating new instance attributes.

LockedClass:
    - A class for preventing users from dynamically creating
    new instance attributes, except if the new instance attribute
    is called 'first_name'.
"""


class LockedClass:
    """
    A class for preventing users from dynamically creating
    new instance attributes.
    """

    def __setattr__(self, name, value):
        err_message = f"'LockedClass' object has no attribute '{name}'"
        if name != "first_name":
            raise AttributeError(err_message)
        object.__setattr__(self, name, value)


# val = LockedClass()
# val.first_name = "Adaku"
# print(val.first_name)
