#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    for i, char in enumerate(str_list):
        if char in "cC":
            str_list[i] = ""
    my_string1 = "".join(str_list)
    return my_string1
