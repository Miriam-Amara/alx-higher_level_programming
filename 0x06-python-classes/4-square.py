#!/usr/bin/python3

"""
A module that defines a Square class
"""


class Square:
    """
    This class that calculates square of a number

    Attributes:
    __size(int): the number to be squared

    Methods:
    area(self): returns the square of the number
    """

    def __init__(self, size=0):
        """
        Initializes the instance attributes

        Args:
        size(int): the number to be squared, default is 0
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the number to be squared

        Returns:
            current value of the number
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set a new value

        Args:
        value(int): the new value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the square of a number
        """
        return self.__size ** 2
