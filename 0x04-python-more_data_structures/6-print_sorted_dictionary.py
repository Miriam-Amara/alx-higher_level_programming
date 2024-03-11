#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_list = []
    new_dict = {}
    for key in a_dictionary:
        keys_list.append(key)
    keys_list.sort()
    for item in keys_list:
        for key, value in a_dictionary.items():
            if item == key:
                new_dict[key] = value
    for key, value in new_dict.items():
        print(f"{key}: {value}")