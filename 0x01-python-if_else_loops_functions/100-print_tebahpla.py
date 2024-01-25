#!/usr/bin/python3
Alpha1 = chr(122)
for i in range(13):
    Alpha2 = chr(ord(Alpha1) - 33)
    print("{}{}".format(Alpha1, Alpha2), end="")
    Alpha1 = chr(ord(Alpha1) - 2)
