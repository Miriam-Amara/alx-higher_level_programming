#!/usr/bin/python3
"""
This module a function that prints a square with the character #.

Function:
def print_square(size) -> None: It prints a square with the character #.
"""


def print_square(size):
    """
    This function prints a square with the character "#".

    Parameter:
    size(int): the size length of the square.

    Returns:
    None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
