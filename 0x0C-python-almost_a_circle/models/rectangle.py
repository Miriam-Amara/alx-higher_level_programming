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

    def validate_attribute(self, attribute, value):
        """Validates all the instance attributes except id."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width; must be positive integer."""
        self.validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height; must be positive integer."""
        self.validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate; must be positive integer or zero."""
        self.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate; must be positive integer or zero."""
        self.validate_attribute("y", value)
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle using '#' symbol."""
        symbol = "#"
        display_symbol = ""

        for i in range(self.__height):
            for _ in range(self.__width):
                display_symbol += symbol
            if i != (self.__height - 1):
                display_symbol += "\n"
        print(display_symbol)

    def __str__(self):
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.__width}/{self.__height}"
        )

    def update(self, *args):
        pass


if __name__ == "__main__":
    rectangle = Rectangle(2, 2)
    rectangle.display()
    print(rectangle)
