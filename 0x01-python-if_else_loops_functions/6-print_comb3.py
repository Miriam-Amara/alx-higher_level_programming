#!/usr/bin/python3
i = 0
while i >= 0 and i <= 8:
    j = i + 1
    while j >= i + 1 and j <= 9:
        print("{}{}".format(i, j), end="\n" if i == 8 and j == 9 else ", ")
        j += 1
    i += 1
