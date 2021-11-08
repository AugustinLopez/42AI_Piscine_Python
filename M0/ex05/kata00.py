#!/usr/bin/env python
"""
This is `kata00`: building a formatted string dynamically from a tuple
"""

t = (19, 42, 21)
length = len(t)
print("The", length, "numbers are:", end=' ')
for n in t:
    length -= 1
    if (length):
        print(n, ",", sep='', end=' ')
    else:
        print(n)
