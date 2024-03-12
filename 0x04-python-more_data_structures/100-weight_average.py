#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_num, sum_weights = (0, 0)
    if not my_list:
        return 0
    for tuples in my_list:
        for i, j in [tuples]:
            mul = i * j
        sum_num += mul
        sum_weights += j
    return sum_num / sum_weights
