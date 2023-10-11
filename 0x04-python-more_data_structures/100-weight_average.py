#!/usr/bin/python3
# a function that returns the weighted average of all integers tuple

def weight_average(my_list=[]):
if not my_list
return 0
number = 0
total_weighted = 0
for tuple in my_list
number += tuple[0] * tuple[1]
total_weighted += tuple[1]
return (number / total weighted)
