#!/usr/bin/env python

from sys import argv
from collections import defaultdict


lst = [y.rstrip().split('|') for y in open(argv[1])]
res=0
part1 = 0
mylen = [6,2,5,5,4,5,6,3,7,6]
for elem in lst:
    p1 = elem[0].strip(' ').split(' ')
    p2 = elem[1].strip(' ').split(' ')
    d = defaultdict(list)
    for mystr in p1:
        if len(mystr) == 2:
            d[1] = mystr
        elif len(mystr) == 4:
            d[4] = mystr
        elif len(mystr) == 3:
            d[7] = mystr
        elif len(mystr) == 7:
            d[8] = mystr
        elif len(mystr) == 5:
            d[3].append(mystr)
        elif len(mystr) == 6:
            d[0].append(mystr)
    for x in d[0]:
        if len(list(set(x) ^ set(d[4]))) == 2:
            d[9] = x
            break
    for x in d[0]:
        if len(list(set(x) ^ set(d[7]))) == 5:
            d[6] = x
            break
    for x in d[0]:
        if x != d[6] and x != d[9]:
            d[0] = x
            break
    for x in d[3]:
        if len(list(set(x) ^ set(d[9]))) == 3:
            d[2] = x
            break
    for x in d[3]:
        if len(list(set(x) ^ set(d[2]))) == 4:
            d[5] = x
            break
    for x in d[3]:
        if len(list(set(x) ^ set(d[2]))) == 2:
            d[3] = x
            break
    y = 0
    for mystr in p2:
        tmp = sorted(mystr)
        for k, v in d.items():
            v = sorted(v)
            if tmp == v:
                y = k + y * 10
                if k in [1,4,7,8]:
                    part1 +=1
                break
    res = res + y
print(part1)
print(res)