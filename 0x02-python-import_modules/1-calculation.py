#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    op = "+-*/"
    func = (add(a, b), sub(a, b), mul(a, b), div(a, b))
    for index in range(4):
        print("{} {} {} = {}".format(a, op[index], b, func[index]))
