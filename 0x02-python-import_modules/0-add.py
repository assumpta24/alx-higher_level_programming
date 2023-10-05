#!/usr/bin/python3

a = 1
b = 2

if __name__ == "__main__":
    from add_0 import add

    #prints the result of the addition 1 + 2 = 3

    print("{} + {} = {}".format(a, b, add(a, b)))
