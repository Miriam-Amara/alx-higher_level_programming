#!/usr/bin/python3

for i in range(97, 123):
    if i == 101 or i == 113:
        i += 1
        continue
    print("{}".format(chr(i)), end="")
    i += 1
