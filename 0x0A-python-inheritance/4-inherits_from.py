#!/usr/bin/python3

"""
This module provides a function to check if
an object is an instance of a class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        Obj: the object to check.
        a_class: the class to check against.

    Returns:
        bool
        True if the object is an instance of any subclass or superclass
        of the specified class; otherwise False.
    """

    if isinstance(obj, a_class):
        if a_class in obj.__class__.__mro__[1:]:
            return True
        else:
            return False


# a = True
# if inherits_from(a, int):
#     print("{} inherited from class {}".format(a, int.__name__))
# if inherits_from(a, bool):
#     print("{} inherited from class {}".format(a, bool.__name__))
# if inherits_from(a, object):
#     print("{} inherited from class {}".format(a, object.__name__))
