#!/usr/bin/python3

"""
my_int Module

Defines a custom integer class, MyInt, that inverts the behavior of the
equality (==) and inequality (!=) operators.
"""


class MyInt(int):
    """
    A custom integer class that inverts the equality operators.

    In this class, '==' returns the result of '!=',
    and '!=' returns the result of '=='.
    """

    def __eq__(self, value):
        """
        Return True if the values are not equal, inverting the equality check.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Return True if the values are equal, inverting the inequality check.
        """
        return self.real == value


# print(issubclass(MyInt, int))
# m = MyInt(3)
# print(m)
