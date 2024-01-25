#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = str(number)
text = "Last digit of"
text1 = "and is less than 6 and not 0"
if number == 0:
    print(f"{text} {number} is {number} and is 0")
elif number > 0:
    if number1[-1] == "0":
        print(f"{text} {number} is {number1[-1]} and is 0")
    elif number1[-1] < "6":
        print(f"{text} {number} is {number1[-1]} {text1}")
    elif number1[-1] > "5":
        print(f"{text} {number} is {number1[-1]} and is greater than 5")
else:
    if number1[-1] == "0":
        print(f"{text} {number} is {number1[-1]} and is 0")
    else:
        print(f"{text} {number} is -{number1[-1]} {text1}")
