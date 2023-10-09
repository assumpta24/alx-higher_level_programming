#!/usr/bin/python3
# a function that replaces an element in a list at a specific position

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list[:])
    copy_of_list = my_list[:]
    copy_of_list[idx] = element
    return (copy_of_list)
