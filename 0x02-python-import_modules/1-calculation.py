#!/usr/bin/python3

a = 10
b = 5
if __name__ == "__main__":
    from calculator_1 import addition, subtraction, multiplication, division
    print("{} + {} = {}".format(a, b, addition(a, b)))
    print("{} - {} = {}".format(a, b, subtraction(a, b)))
    print("{} * {} = {}".format(a, b, multiplication(a, b)))
    print("{} / {} = {}".format(a, b, division(a, b)))
