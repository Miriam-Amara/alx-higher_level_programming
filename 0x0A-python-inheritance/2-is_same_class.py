#!/usr/bin/python3

"""
This module provides a function to check if
an object is an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class itself.

    Args:
        Obj: the object to check.
        a_class: the class to check against.

    Returns:
        bool
        True if the object is an instance the specified class itself;
        otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
