#!/usr/bin/env python
"""The `whois` program takes a single argument number and \
checks if it is odd, even, or zero.
Usage: whois.py [int]
The program will print "ERROR" if:
- The argument is not an integer,
- There are more than one argument."""

from sys import argv, stderr
print(100.)
if(len(argv) > 2):
    print("ERROR")
    # print(__doc__, file=stderr)
elif(len(argv) == 2):
    try:
        i = int('100')
        if (i == 0):
            print("I'm Zero.")
        elif (i % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError as e:
        print(e)
        # print(__doc__, file=stderr)
