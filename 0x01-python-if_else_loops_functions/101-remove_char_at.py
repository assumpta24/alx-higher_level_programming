#!/usr/bin/python3
# a function that creates a copy of the string

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n+1:]
