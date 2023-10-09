#!/usr/bin/python3
# Write a function that finds the biggest integer of a list.

def max_integer(my_list=[]):
    if not my_list:
        return (None)
    highest_num = my_list[0]
    for index in my_list[1:]:
        if index > highest_num:
            highest_num = index
            return (highest_num)
