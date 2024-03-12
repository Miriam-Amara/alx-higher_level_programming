#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for nums in matrix:
        matrix1 = []
        for i in range(len(nums)):
            square_num = nums[i] ** 2
            matrix1.append(square_num)
        matrix2.append(matrix1)
    return matrix2
