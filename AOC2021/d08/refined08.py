#!/usr/bin/env python

from sys import argv

p1 = 0
p2 = 0
for x, y in [y.rstrip().split('|') for y in open(argv[1])]:
    l = {len(s): set(s) for s in x.split()}
    n = ''
    for o in map(set, y.split()):
        mask = (len(o), len(o&l[4]), len(o&l[2]))
        if len(o) in (2,3,4,7): p1 += 1
        if mask[0] == 2: n += '1'
        elif mask[0] == 3: n += '7'
        elif mask[0] == 4: n += '4'
        elif mask[0] == 7: n += '8'
        elif mask[1] == 2: n += '2'
        elif mask[1] == 4: n += '9'
        elif mask == (5,3,1): n += '5'
        elif mask == (5,3,2): n += '3'
        elif mask == (6,3,1): n += '6'
        elif mask == (6,3,2): n += '0'
    p2 += int(n)
print(p1)
print(p2)