#!/usr/bin/python3

"""
This module provides the Square Class for creating square shapes.
The Square class inherits functionality from
Rectangle class (its parent class), which in turn inherits
from the BaseGeometry class.

The size of the square is validated by the integer_validator method
from the BaseGeometry class. The class also includes a method to
calculate the area of the square.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class used to create square shapes.

    Inherits from Rectangle class, which validates size
    as a positive integer using the integer_validator
    from the BaseGeometry class.
    """

    def __init__(self, size):
        """
        Initialize a square instance.

        The size is passed to the Rectangle constructor,
        which validates it as a positive integer using
        the integer_validator method from BaseGeometry.

        Args:
            size(int): The size of the square, must be a
            positve integer.
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size


# s = Square(4)

# print(s)
# print(s.area())
# print(s.__class__.__mro__)
# print(dir(s))
