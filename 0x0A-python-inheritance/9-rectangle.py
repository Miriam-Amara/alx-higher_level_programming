#!/usr/bin/python3

"""
Rectangle module

This module provides the Rectangle class for defining rectangle shapes
and inherits functionality from the BaseGeometry class.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class used to define rectangle shapes,
    inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the instance attributes and validates
        width and height using integer_validator.

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calulates the area of the rectangle.
        
        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle class
        in the format '[Rectangle] <width>/<height>'.

        Returns:
            str: String representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


# r = Rectangle(3, 5)

# print(r)
# print(r.area())
