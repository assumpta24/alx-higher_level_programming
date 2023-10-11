#!/usr/bin/python3
# a function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    new_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[row][col] = matrix[row][col] ** 2
            return (new_matrix)
