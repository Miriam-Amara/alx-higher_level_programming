#!/usr/bin/python3

i = 0

while i >= 0 and i <= 8:
    j = i + 1
    while j >= i + 1 and j <= 9:
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}, ", end="")
        j += 1
    i += 1
