#!/usr/bin/python3

for i in range(0,100):
    if (i >= 0 and i <= 9):
        i = '0' + str(i) + ", "
    elif (i == 99):
        i = '99'
    else:
        i = str(i) + ", "
    print(f"{i}", end = '')
print('\n')
