#!/usr/bin/python3
# Write a function that finds the biggest integer of a list.

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    highest_num = my_list[0]
    for index in range(len(my_list)):
        if my_list > highest_num:
            highest_num = my_list[index]
            return highest_num
