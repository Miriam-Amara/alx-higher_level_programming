#!/usr/bin/python3

"""
A module that defines a Square class
"""


class Square:
    """
    This class calculates square of a number

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """
        Returns the square of a number
        """
        return self.__size ** 2  