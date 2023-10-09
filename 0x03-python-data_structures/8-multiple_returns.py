#!/usr/bin/python3
# function that returns a tuple with the length of a string and

def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
