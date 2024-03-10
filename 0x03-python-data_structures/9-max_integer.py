#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    if my_list != []:
        for num in my_list:
            if num > max_value:
                max_value = num
        return max_value
    return None
