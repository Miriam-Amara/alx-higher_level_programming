#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    new_list = []
    for num in my_list:
        if num == my_list[idx]:
            my_list[idx] = element
        new_list.append(num)
    return new_list
