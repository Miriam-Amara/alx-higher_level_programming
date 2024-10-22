#!/usr/bin/python3

"""
This module provides 'append_write' function, which appends a string
to a file using UTF-8 encoding and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a file using UTF-8 encoding
    and creates the file if it does not exist.

    Args:
        filename (str): The name of the file to be written to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, "a", encoding="utf-8") as file:
        no_of_chars_written = file.write(text)
    return no_of_chars_written
