#!/usr/bin/python3

"""
This module provides append_after function, which inserts
a line of text to a file, after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    the given string.

    Args:
        filename (str): The file to read from and write to.
        search_string (str): The given string to look for.
        new_string (str): The string to be inserted after each
        line with the given string.
    """

    with open(filename, "r", encoding="utf-8") as file:
        content = ""
        while True:
            line = file.readline()
            if search_string in line:
                line += new_string + "\n"
            elif not line:
                break
            content += line

    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(content)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "C is fun!")
