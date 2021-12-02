#!/usr/bin/env python

from sys import argv


tab = [0]
with open(argv[1]) as fd:
    for line in fd.readlines():
        x = int(line)
        for i in range(len(tab[-3:])):
            tab[len(tab) - i - 1] += x
        tab.append(0)
tab.pop()
val = tab[0]
inc = 0
for elem in tab[1:]:
    x = elem
    if x > val:
        inc += 1
    val = x
print(inc)
