#!/usr/bin/python3

"""
This module provides `load_from_json_file` function,
which creates an object from a file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a file.

    Args:
        filename (str): The file from which the object is created.

    Return:
        Any: The object created.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = json.load(file)
    return content


# filename = "my_list.json"
# my_list = load_from_json_file(filename)
# print(my_list)
# print(type(my_list))

# filename = "my_dict.json"
# my_dict = load_from_json_file(filename)
# print(my_dict)
# print(type(my_dict))

# try:
#     filename = "my_set_doesnt_exist.json"
#     my_set = load_from_json_file(filename)
#     print(my_set)
#     print(type(my_set))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     filename = "my_fake.json"
#     my_fake = load_from_json_file(filename)
#     print(my_fake)
#     print(type(my_fake))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
