#!/usr/bin/python3
# a function that prints a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for numbers in rows:
            print("{:d}".format(numbers), end=" ")
            print()
