#!/usr/bin/python3
# a function that finds all multiples of 2 in a list.

def divisible_by_2(my_list=[]):
    multiples_of_two = []
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            multiples_of_two.append(True)
        else:
            multiples_of_two.append(False)
            return multiples_of_two
