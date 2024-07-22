#!/usr/bin/python3
"""
This module provides a Rectangle class
that defines a rectangle.

Classes:
    Rectangle: Represent a rectangle with widhth and height.

Usage Example:
    Rectangle = __import__("1-rectangle").Rectangle
    my_rectangle = Rectangle()
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    __width (int): The rectangle's width.
    __height (int): The rectangle's height.
    """

    def __init__(self, width=0, height=0):
        """
        Constructs necessary attributes for the rectangle object.

        Args:
        width (int): The rectangle's width.
        height (int): The rectangle's height.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
