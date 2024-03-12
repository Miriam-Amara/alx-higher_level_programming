#!/usr/bin/pyth0n3
def only_diff_elements(set_1, set_2):
    list_elements = list(set_1) + list(set_2)
    for item in set_1:
        if item in set_2:
            list_elements.remove(item)
            list_elements.remove(item)
    return set(list_elements)