#!/usr/bin/python3
def magic_string():
    magic_string.count_call += 1; return "BestSchool, " * (magic_string.count_call - 1) + "BestSchool"
magic_string.count_call = 0
