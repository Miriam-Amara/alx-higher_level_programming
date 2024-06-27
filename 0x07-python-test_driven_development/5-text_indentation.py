#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :

Function:
text_indentation(text) -> None
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of
    these characters: ., ? and :

    Parameter:
    text(str) - the text that will be evaluated

    Return:
    None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 2

        else:
            print(text[i], end="")
            i += 1
