#!/usr/bin/python3
# a function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    sorted_ord = sorted(a_dictionary.keys())
    for index in sorted_ord:
        print("{}: {}".format(index, a_dictionary.get(index)))
