#!/usr/bin/python3
"""
Module that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    A function that multiplies two matrices.
    It returns a list of lists containing the result.
    """

    # checks if args are list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # checks if args are list of lists
    if not all(isinstance(row_a, list) for row_a in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row_b, list) for row_b in m_b):
        raise TypeError("m_b must be a list of lists")

    # checks if args are empty list
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # checks if list elements are int or float and if the matrix is a rectangle
    for row in m_a:
        for num_a in row:
            if not isinstance(num_a, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for element in m_b:
        for num_b in element:
            if not isinstance(num_b, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(element) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    # checks if row of m_a has the same size as col of m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):
        row_mul = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                mul = m_a[i][k] * m_b[k][j]
                sum += mul
            row_mul.append(sum)
        new_matrix.append(row_mul)
    return new_matrix
