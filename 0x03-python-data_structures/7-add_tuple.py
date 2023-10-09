#!/usr/bin/python3
#  a function that adds 2 tuples.

def add_tuple(tuple_a=(), tuple_b=()):
    result_1 = tuple_a[:2] + (0, 0)
    result_2 = tuple_b[:2] + (0, 0)

    total = (result_1[0] + result_2[0], result_1[1] + result_2[1])
    return total
