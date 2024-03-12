#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    if value not in a_dictionary.values():
        return a_dictionary
    for key, item in a_dictionary.items():
        if item == value:
            key_list.append(key)
    for element in key_list:
        del a_dictionary[element]
    return a_dictionary
