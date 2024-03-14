#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    solution = []
    for i in range(list_length):
        try:
            solution.append(my_list_1[i]/ my_list_2[i])
        except ZeroDivisionError:
            solution.append(0)
            print("division by 0")
        except TypeError:
            solution.append(0)
            print("wrong type")
        except IndexError:
            solution.append(0)
            print("out of range")
    return (solution)