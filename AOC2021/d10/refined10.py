#!/usr/bin/env python

from sys import argv

d = {']':'[',')':'(','}':'{', '>':'<'}
r = {'(':1, '[':2, '{':3, '<':4, ')':3, ']':57, '}':1197, '>':25137}
p1 = 0
p2 = []
for x in open(argv[1]):
    opening = []
    for c in list(x.rstrip()):
        if c in d.values:
            opening.append(c)
        elif opening.pop() != d[c]:
            p1 += r[c]
            break
    else: # when break is not called
        tmp = 0
        for c in opening[::-1]:
            tmp = tmp * 5 + r[c]
        p2.append(tmp)
print(p1)
print(sorted(p2)[len(p2) // 2])