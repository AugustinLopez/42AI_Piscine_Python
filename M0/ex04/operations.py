#!/usr/bin/env python
"""The `operation` programs takes two numbers as arguments and calculates:
- Sum,
- Difference,
- Product,
- Quotient,
- Remainder.
"""
from sys import argv

argc = len(argv)
if (argc > 3):
    print("InputError: too many arguments")
elif (argc < 3):
    print("InputError: not enough arguments")
if (argc != 3):
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n\tpython operations.py 10 3")
else:
    try:
        left = int(argv[1])
        right = int(argv[2])
        s = left + right
        d = left - right
        p = left * right
        print("Sum:        ", s)
        print("Difference: ", d)
        print("Product:    ", p)
        try:
            q = left / right
            r = left % right
            print("Quotient:   ", q)
            print("Remainder:  ", r)
        except ZeroDivisionError:
            print("Quotient:    ERROR (division by zero)")
            print("Remainder:   ERROR (modulo by zero)")
    except ValueError:
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n\tpython operations.py 10 3")
