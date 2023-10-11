#!/usr/bin/python3
# a function that adds all unique integers in a list

def uniq_add(my_list=[]):
    unique_list = set(my_list)
    number = 0
    for index in unique_list:
        number += index
        return number
