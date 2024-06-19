#!/usr/bin/python3
"""
This module contains function that divides all elements of a matrix.

Function:
matrix_divided(matrix, div) -> list: Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    This functions divides all elements of a matrix and returns a new matrix.

    Parameters:
    matrix(list): A list of lists containing numbers(int/float) to be divided.
    div(int or float): The number that divides each element of a matrix.

    Returns:
    List: A new matrix
    """

    new_matrix = []
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "each row of the matrix must have the same size"

    # checks for valid div value
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # checks that matrix is a list of lists
    if not isinstance(matrix, list):
        raise TypeError(err1)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(err1)

    # checks that each row of the matrix has the same size
    length = len(matrix[0])
    for row in matrix:
        inner_matrix = []
        if len(row) == length:
            for num in row:
                if isinstance(num, (int, float)):
                    result = num / div
                    inner_matrix.append(round(result, 2))
                else:
                    raise TypeError(err1)
            new_matrix.append(inner_matrix)
        else:
            raise TypeError(err2)

    return new_matrix
