#!/usr/bin/python3

"""
This module provides `save_to_json_file` function,
which writes an object to a file using UTF-8 encoding and in JSON format.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using UTF-8 encoding and
    JSON representation.

    Args:
        my_obj (Any): The object to be serialized and written to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)


# filename = "my_list.json"
# my_list = [1, 2, 3]
# save_to_json_file(my_list, filename)

# filename = "my_dict.json"
# my_dict = {
#     'id': 12,
#     'name': "John",
#     'places': [ "San Francisco", "Tokyo" ],
#     'is_active': True,
#     'info': {
#         'age': 36,
#         'average': 3.14
#     }
# }
# save_to_json_file(my_dict, filename)

# try:
#     filename = "my_set.json"
#     my_set = { 132, 3 }
#     save_to_json_file(my_set, filename)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
