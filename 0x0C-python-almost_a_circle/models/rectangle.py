#!/usr/bin/python3

"""
Module for Rectangle class that inherits from Base.
"""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle defined by its width, height, and position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle with given dimensions and position."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width; must be positive."""
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height; must be positive."""
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate; must be an integer or float."""
        if not isinstance(value, (int, float)):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate; must be an integer or float."""
        if not isinstance(value, (int, float)):
            raise TypeError("y must be an integer")
        self.__y = value


if __name__ == "__main__":
    rectangle = Rectangle(5, 8)
    print(rectangle.width)
