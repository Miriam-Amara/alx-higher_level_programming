#!/usr/bin/python3
str = "Holberton School"
print(str * 3 + "\n" + str[0:9])
print(f"\n{str*3}\n{str[0:9]}")
print("\n%s\n%s" % (str * 3, str[0:9]))
print("\n{}\n{}".format(str * 3, str[0:9]))
