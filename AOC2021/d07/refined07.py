#!/usr/bin/env python

from sys import argv

def sumi(x):
    return x * (x + 1) // 2

lst = [*map(int, open(argv[1]).readline().split(','))]
lst.sort()
med = lst[len(lst) // 2]
avg = sum(lst) // len(lst)
print(sum([abs(i - med) for i in lst]))
print(sum([sumi(abs(i - avg)) for i in lst]))
print(sum([sumi(abs(i - avg+1)) for i in lst]))
print(sum([sumi(abs(i - avg-1)) for i in lst]))