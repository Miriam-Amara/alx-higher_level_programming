#!/usr/bin/python3

"""
This module defines a function that writes a string
to a file using UTF-8 encoding and returns the number
of characters written.
"""


def write_file(filename="", text=""):
    """
    Overwrites the content of a file using utf-8 encoding
    and creates the file if it doesn't exist.

    Args:
        filename (str): The file name for writing the string.
        text (str): The string to be written.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        no_of_chars_written = file.write(text)
    return no_of_chars_written


# print(write_file("my_file.txt", "My name is: "))
