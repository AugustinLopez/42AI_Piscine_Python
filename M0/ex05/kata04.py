#!/usr/bin/env python
"""
This is `kata04`: print formatted information
"""

t = (0, 4, 132.42222, 10000, 12345.67)

print("module_", '0' * (len(str(t[0])) == 1), t[0], sep='', end=',')
print(" ex_", '0' * (len(str(t[1])) == 1), t[1], sep='', end=' ')
print(": %.2f, %.2e, %.2e" % (t[2], t[3], t[4]))
