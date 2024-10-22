#!/usr/bin/python3

def read_file(filename=""):
    with open(filename) as f:
        content = f.read()
        print(content)

# read_file("my_file.txt")
