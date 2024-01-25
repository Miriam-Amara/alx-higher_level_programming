#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        alpha = str[i]
        if str[i] >= "a" and str[i] <= "z":
            num = ord(str[i]) - 32
            alpha = chr(num)
            if i == len(str) - 1:
                alpha = alpha + "\n"
        print("{}".format(alpha), end="")

uppercase("Holberton school")
