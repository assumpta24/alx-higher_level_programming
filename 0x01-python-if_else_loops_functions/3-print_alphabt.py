#!/usr/bin/python3
for chr_code in range(97, 123):
    if chr(chr_code) != "q" and chr(chr_code) != "e":
        print("{}".format(chr(chr_code)), end="")
