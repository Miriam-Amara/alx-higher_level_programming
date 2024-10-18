#!/usr/bin/python3

"""
BaseGeometry Module

This module defines the BaseGeometry class,
which serves as a base class for geometry shapes.
"""


class BaseGeometry:
    """
    A base class for geometry shapes.

    This class serves as a blueprint for creating
    specific geometry shapes.
    """

    def area(self):
        """
        Calculate the area of the geometry shape.

        Ths method raises an exception indicating that the
        area method is not implemented. Subclasses must overide
        this method to provide their specific calculation.
        """
        raise Exception("area() is not implemented")


# bg = BaseGeometry()

# try:
#     print(bg.area())
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
