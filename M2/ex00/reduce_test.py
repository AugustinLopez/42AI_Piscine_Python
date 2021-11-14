#!/usr/bin/env python

from functools import reduce
from ft_reduce import ft_reduce

function = lambda x: x + 1
iterable = [1, 2, 3]
try:
    print(ft_reduce(None, iterable = iterable))
except Exception as e:
    print(e)
try:
    print(ft_reduce(function, None))
except Exception as e:
    print(e)
print(ft_reduce((lambda x, y: x + y), [1]))
print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))

def do_sum(x1, x2):
    return x1 + x2

print(ft_reduce(do_sum, [1, 2, 3, 4]))

# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
print(reduce(lambda u, v: u + v, lst))
