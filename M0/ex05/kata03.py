#!/usr/bin/env python
"""
This is `kata03`: print a string of a least 42 characters
"""

test = ["the right format", "hello", "aaaaaaaaaaaaaaaaaaa", ""]
for phrase in test:
    length = len(phrase)
    x = 42 - length
    if (x > 0):
        print("-" * x, end='')
    print(phrase, end='')
