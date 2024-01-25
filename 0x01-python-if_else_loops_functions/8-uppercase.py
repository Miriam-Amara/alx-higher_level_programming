#!/usr/bin/python3
def uppercase(str):
    if str == "":
        alpha = " "
    for i in range(len(str)):
        alpha = str[i]
        if str[i] >= "a" and str[i] <= "z":
            num = ord(str[i]) - 32
            alpha = chr(num)
        print("{}".format(alpha), end="" if i != len(str) - 1 else '\n')
