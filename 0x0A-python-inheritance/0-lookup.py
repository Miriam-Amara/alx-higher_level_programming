#!/usr/bin/python3

"""
This module provides lookup function that returns
list of available attributes and methods for an object.
"""


def lookup(obj):
    """
    Returns the attributes and methods of the given object.

    Args:
    obj(any): The object to check for the attributes and methods.

    Returns:
        list
        The list of the attributes and methods of the given object.
    """
    return dir(obj)


# print(lookup(int))
