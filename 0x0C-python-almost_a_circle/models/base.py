#!/usr/bin/python3

"""
base module

This module provides the Base class.
"""


class Base:
    """
    A base class that manages id assignment for its instances.

    Attributes:
        __nb_objects (int): A private class attribute that tracks the number
        of instances for auto-incrementing ids.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int, optional): The id for the instance. If None, the id
            is auto-incremented using the class-level counter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
