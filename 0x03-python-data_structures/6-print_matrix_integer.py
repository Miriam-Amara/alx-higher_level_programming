#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nums in matrix:
        for i, num in enumerate(nums):
            if i == 2:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=" ")