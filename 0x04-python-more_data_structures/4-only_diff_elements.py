#!/usr/bin/pyth0n3
def only_diff_elements(set_1, set_2):
    list1 = list(set_1)
    list2 = list(set_2)
    list3 = list1 + list2
    for item in list1:
        if item in list2:
            list3.remove(item)
            list3.remove(item)
    return set(list3)