#!/usr/bin/python3

"""
This module provides `class_to_json` function,
which returns the dictionary description of an object
with simple data structures suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object
    with simple data structures (list, dict, str, int, bool)
    for JSON serializaton.

    Args:
        obj (Any): A class instance to be converted into a dictionary.

    Returns:
        dict: A dictionary containing all attributes of the object,
        suitable for JSON serialization.
    """
    return obj.__dict__
