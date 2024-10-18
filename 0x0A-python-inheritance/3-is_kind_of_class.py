#!/usr/bin/python3

"""
This module provides a function to check if
an object is an instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a given class, or
    if the object is an instance of a class that
    inherited from the specified class.

    Args:
        Obj: the object to check.
        a_class: the class to check against.

    Returns:
        bool
        True if the object is an instance the class;
        otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
