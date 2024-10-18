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


# r = Rectangle(3, 5)

# print(r)
# print(dir(r))

# try:
#     print("Rectangle: {} - {}".format(r.width, r.height))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r2 = Rectangle(4, True)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
