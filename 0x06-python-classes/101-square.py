#!/usr/bin/python3

"""
A module that contains a Square class
"""


class Square:
    """
    This class that calculates square of a number

    Attributes:
    __size(int): the number to be squared

    Methods:
    area(self): returns the square of a number
    my_print(self): represents the square of a number with #
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the instance attributes

        Args:
        size(int): the number to be squared, default is 0
        position(tuple): determines how number of spaces to be added
        """
        self.__size = None
        self.size = size
        self.__position = None
        self.position = position

    @property
    def size(self):
        """
        Gets the number to be squared

        Returns:
            current value of the number
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set a new value

        Args:
        value(int): the new value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Gets a tuple containing positions of spaces to be added

        Returns:
            the current value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set a new tuple

        Arg:
        value(tuple): the new tuple to set
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not (
                (isinstance(value[0], int) and value[0] >= 0)
                and (isinstance(value[1], int) and value[1] >= 0)
            )
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the square of a number
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method represents the square of a number with #
        """
        if self.__size != 0:
            if self.__position[1] > 0:
                print()
            for _ in range(self.__size):
                for i in range(self.__size + self.__position[0]):
                    if i < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
        else:
            print()

    def __repr__(self):
        self.my_print()
        return ""
