#!/usr/bin/python3
"""
This module provides functions for basic arithmetic operations.

Functions:
add_integer(a, b=98) -> int: Returns the sum of a and b.

Usage:
Import the module and call the function with at least one argument:

import 0-add_integer

result = 0-add_integer.add_integer(3, 4)
print(result) #Output: 7
"""


def add_integer(a, b=98) -> int:
    """
    This function computes the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number. It is by default 98.

    Returns:
    int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except Exception:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except Exception:
        raise TypeError("b must be an integer")
    return a + b
