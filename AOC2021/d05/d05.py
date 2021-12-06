#!/usr/bin/env python

from sys import argv
import numpy as np

lst = [x.rstrip().split(' -> ') for x in open(argv[1])]
res = [[x.split(','), y.split(',')] for x, y in lst]

coordinate = {}
for elem in res:
    x0, x1 = int(elem[0][0]), int(elem[1][0])
    y0, y1 = int(elem[0][1]), int(elem[1][1])
    if not(x0 == x1 or y0 == y1):
        if abs(x0 - x1) != abs(y0 - y1):
            continue
        if x0 > x1:
            rng = range(x0, x1-1, -1)
        else:
            rng = range(x0, x1 + 1)
        y = y0
        i = -1 if y0 > y1 else 1
        for x in rng:
            k = str(x) + ',' + str(y)
            y = y + i
            if k in coordinate:
                coordinate[k] += 1
            else:
                coordinate[k] = 1
        continue
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0
    if x0 != x1:
        for x in range(x0, x1 + 1):
            k = str(x) + ',' + str(y0)
            if k in coordinate:
                coordinate[k] += 1
            else:
                coordinate[k] = 1
    else:
        for y in range(y0, y1 + 1):
            k = str(x0) + ',' + str(y)
            if k in coordinate:
                coordinate[k] += 1
            else:
                coordinate[k] = 1
print(coordinate)
new_data = {k: v for k, v in coordinate.items() if v > 1}
print(len(new_data))