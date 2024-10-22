#!/usr/bin/python3
"""
This module provides add_attribute function
that adds a new attribute to an object if possible.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        name (str): The new attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object cannot accept a new attribute.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
