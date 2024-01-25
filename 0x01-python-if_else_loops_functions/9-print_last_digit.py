#!/usr/bin/python3


def print_last_digit(number):
    number = str(number)
    for i in range(len(number)):
        if i == len(number) - 1:
            print(f"{number[i]}", end="")
            return number[i]
