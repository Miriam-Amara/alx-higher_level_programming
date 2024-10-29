#!/usr/bin/python3

"""
This module provides pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to a specified number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists, where each inner list contains integers
        representing a row of Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = []
    value = 0

    for i in range(n):
        nums = []
        index = 0
        for j in range(i + 1):
            if j == 0 or j == i:
                nums.append(1)
            else:
                value = triangle[i - 1][index] + triangle[i - 1][index + 1]
                nums.append(value)
                index += 1
        triangle.append(nums)
    return triangle


if __name__ == "__main__":
    print(pascal_triangle(5))
