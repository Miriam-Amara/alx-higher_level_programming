#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    new_dict = {}
    for key in keys:
        new_dict.update({key: a_dictionary[key]})
    for key, value in new_dict.items():
        print(f"{key}: {value}")
