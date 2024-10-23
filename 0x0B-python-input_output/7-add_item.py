#!/usr/bin/python3

"""
This module provides `add_item` function that adds all arguments
to a Python list, and then save them to a file
"""


import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item():
    """
    Adds all arguments to a Python list, and then save them to a file.
    """
    arguments = sys.argv[1:]
    filename = "add_item.json"

    try:
        current_list = load_from_json_file(filename)
    except FileNotFoundError:
        current_list = []
    for arg in arguments:
        current_list.append(arg)
    save_to_json_file(current_list, filename)


if __name__ == "__main__":
    add_item()
