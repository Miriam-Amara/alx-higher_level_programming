#!/usr/bin/python3
"""
This module provides a Rectangle class
that defines a rectangle.

Classes:
    Rectangle: Represent a rectangle with widhth and height.

Usage Example:
    Rectangle = __import__("1-rectangle").Rectangle
    my_rectangle = Rectangle()
    my_rectangle = Rectangle(2, 3)
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    __width (int): The width of the rectangle. Defaults to 0.
    __height (int): The height of the rectangle. Defaults to 0.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructs necessary attributes for the rectangle object.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculates the area of a rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calulates the perimeter of a rectangle.

        Returns:
            int: The perimeter of the rectangle,
            or 0 if either width or height is 0.

        If either the width or height is zero,
        the perimeter is calculated as zero.
        Else, the perimeter is calculated as (width + length) * 2.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perimeter = (self.__width + self.__height) * 2
            return perimeter

    def __str__(self):
        """
        Returns a user friendly str representation of Rectangle class.
        """
        str_rep = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for _ in range(self.__width):
                    str_rep += str(self.print_symbol)
                if i != (self.__height - 1):
                    str_rep += "\n"
            return str_rep

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle
        is about to be destroyed.
        """
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
