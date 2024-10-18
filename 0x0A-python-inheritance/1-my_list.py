#!/usr/bin/python3

"""
This module provides a class that sorts a list in ascending order
without modifying the original list.
"""


class MyList(list):
    """
    A class to sort a list.
    """

    def print_sorted(self):
        """
        Sorts a list in ascending order without
        modifying the original list.

        Returns:
            list: The newly sorted list.
        """
        new_list = sorted(self)
        return new_list
