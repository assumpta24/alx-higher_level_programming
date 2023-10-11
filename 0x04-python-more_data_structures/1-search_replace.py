#!/usr/bin/python3
# a function that replaces all occurrences of an element

def search_replace(my_list, search, replace):
    result_list = list(map(lambda e: replace if e == search else e, my_list))
    return result_list
