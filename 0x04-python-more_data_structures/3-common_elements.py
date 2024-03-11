#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set({})
    new_list = list(set_1) + list(set_2)
    for i, item in enumerate(new_list):
        del new_list[i]
        if item in new_list:
            set_3.add(item)
    return(set_3)