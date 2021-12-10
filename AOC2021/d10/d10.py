#!/usr/bin/env python

from sys import argv

d1 = {']':'[',')':'(','}':'{', '>':'<'}
c1 = {')':3, ']': 57, '}': 1197, '>': 25137}
p2 = []
res = 0
for x in open(argv[1]):
    opening = []
    z = False
    for c in list(x.rstrip()):
        if c in "[({<":
            opening.append(c)
        elif opening[-1] != d1[c]:
            res += c1[c]
            z = True
            break
        else:
            opening.pop()
    if z == False:
        p2.append(opening)
print(res)

c2 = {'(':1,'[':2,'{':3, '<':4}
res = []
for elem in p2:
    tmp=0
    for c in elem[::-1]:
        tmp = tmp * 5 + c2[c]
    res.append(tmp)
res.sort()
print(res[len(res) // 2])
