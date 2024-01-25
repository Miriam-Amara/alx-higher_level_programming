#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i] >= "a" and str[i] <= "z":
            num = ord(str[i]) - 32
            alpha = chr(num)
            if i == len(str) - 1:
                alpha = alpha + "\n"
            print(f"{alpha}", end="")
