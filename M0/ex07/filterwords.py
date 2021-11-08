#!/usr/bin/env python
"""The `filterword` program find all word in a string that contains more than \
`n` non-punctuations/whitespaces characters.
Usage: filterword [string] [int n]
The program use RegEx to replace all punctuations characters by space, \
then split the string using space as separators.
"""
from sys import argv
import string
import re


i = len(argv) - 1
if(i != 2):
    print("ERROR")
else:
    error_str = 1
    error_num = 0
    try:
        num = int(argv[1])
    except ValueError:
        error_str = 0
    try:
        num = int(argv[2])
    except ValueError:
        error_num = 1
    text = argv[1]
    if (error_str + error_num != 0):
        print("ERROR")
    else:
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        out = regex.sub(' ', text)
        listing = out.split()
        result = []
        for elem in listing:
            if (len(elem) > num):
                result.append(elem)
        print(result)
