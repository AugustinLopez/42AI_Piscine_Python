#!/usr/bin/env python
"""
This is `kata03`: print a string of a least 42 characters
"""

# print("{:->42}".format(phrase), end = '')
phrase = "The right format"
length = len(phrase)
x = 42 - length
if (x > 0):
    print("-" * x, end='')
print(phrase, end='')
