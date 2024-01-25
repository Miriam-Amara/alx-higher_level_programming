#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    print(f"{int(number[-1])}", end="")
    return int(number[-1])
