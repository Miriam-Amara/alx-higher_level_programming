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

    def integer_validator(self, name, value):
        """
        Vaidates that the given value is an positive integer.

        Args:
            name(str): The name of the variable being validated.
            value(any): The value to validate as positive integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
