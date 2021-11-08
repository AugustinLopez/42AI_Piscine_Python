#!/usr/bin/env python
"""The `exec.py` program:
 - take a string as argument,
 - reverse uppercase and lowercase,
 - reverse the order of the string.
If the program receives more than one arguments, each arguments are merged
into a single string using a ' ' (space) separator."""

from sys import argv, stderr

# if (len(argv) - 1 <= 0):
#     print(__doc__, file=stderr)
for i in range(len(argv) - 1, 0, -1):
    result = ''.join(c.lower() if c.isupper() else
                     c.upper() for c in reversed(argv[i]))
    if (i > 1):
        print(result, end=" ")
    else:
        print(result)
