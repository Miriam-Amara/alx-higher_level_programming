#!/usr/bin/python3
"""
This module contains function that prints first name and last name.

Function:
say_my_name(first_name, last_name="") -> None: Prints first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints "My name is <first name> <last name>".

    Parameters:
    first_name(str): The first name.
    last_name(str): The last name set to default - empty string.

    Returns:
    None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
