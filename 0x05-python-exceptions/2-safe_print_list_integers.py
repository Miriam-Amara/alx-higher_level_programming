#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            int(my_list[i])
    except ValueError:
        pass
    j = 0
    for i in range(x):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]), end="")
            j += 1
    print()
    return j
