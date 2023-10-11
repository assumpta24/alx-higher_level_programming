#!/usr/bin/python3
# a function that returns the number of keys in a dictionary.

def number_keys(a_dictionary):
    total = 0
    num_keys = list(a_dictionary.keys())
    for index in num_keys:
        total += 1
        return total
