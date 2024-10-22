#!/usr/bin/python3

"""
This module provides read_file function that
reads the contents of a file.
"""


def read_file(filename=""):
    """
    Opens and reads the contents of a file.

    Args:
        filename (str): Name of the file to be read.
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
    print(content)


# read_file("my_file.txt")
