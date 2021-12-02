#!/usr/bin/env python

from sys import argv


lst = [int(x) for x in open(argv[1])]
# part1
print(sum(x < y for x, y in zip(lst, lst[1:])))
# part2
# print(sum(a + b + c < b + c + d for a, b, c, d in zip(lst, lst[1:], lst[2:], lst[3:])))
print(sum(a < d for a, d in zip(lst, lst[3:])))
