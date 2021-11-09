#!/usr/bin/env python
"""
This is `kata00`: building a formatted string dynamically from a tuple
"""

test = [(19, 42, 21), (), (1, 2, 3, 4)]

for t in test:
    length = len(t)
    print("The", length, "numbers are:", end=' ')
    if (length == 0):
        print("")
    for n in t:
        length -= 1
        if (length):
            print(n, ",", sep='', end=' ')
        else:
            print(n)
