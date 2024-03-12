#!/usr/bin/python3
def common_elements(set_1, set_2):
    elements = set(list(set_1) + list(set_2))
    common_elements = []
    for value in elements:
        if value in set_1 and value in set_2:
            common_elements.append(value)
    return common_elements