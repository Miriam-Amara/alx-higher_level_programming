#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list = tuple(my_list)
    copy_list = list(my_list)
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    copy_list[idx] = element
    return copy_list
