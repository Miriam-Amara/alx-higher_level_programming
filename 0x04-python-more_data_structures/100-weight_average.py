#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_num = 0
    weights = []
    if not my_list:
        return 0
    for tuples in my_list:
        for i, j in [tuples]:
            weights.append(j)
            mul = i * j
        sum_num += mul
    weight_average = sum_num / sum(weights)
    return weight_average