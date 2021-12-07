#!/usr/bin/env python

from sys import argv
from statistics import median, mean
from math import floor

def my_initial_2nd_part(lst):
    med = median(lst)
    mem = -1
    xx = 0
    for x in range(1000):
        z = 0
        y = 0
        for elem in lst:
            tmp1 = abs(elem - med - x)
            tmp2 = abs(elem - med + x)
            z += tmp1 * (tmp1 + 1) / 2
            y += tmp2 * (tmp2 + 1) / 2
        if mem == -1 or min(mem, z) == z:
            mem = z
            xx = med + x
        if min(mem, y) == y:
            mem = y
            xx = med - x
    print(int(mem), end = ' ')
    print(int(xx))


lst = [*map(int, open(argv[1]).readline().split(','))]
x = median(lst)
x1 = floor(mean(lst))
x2 = x1 + 1
z = z1 = z2 = 0
for elem in lst:
    z += abs(elem - x)
    z1 += abs(x1 - elem) * (abs(x1 - elem) + 1) // 2
    z2 += abs(x2 - elem) * (abs(x2 - elem) + 1) // 2
print(int(z))
print(int(min(z1, z2)))