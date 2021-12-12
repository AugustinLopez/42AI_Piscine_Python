#!/usr/bin/env python3

from sys import argv
from copy import copy

lst = [x.rstrip().split('-') for x in open(argv[1])]
d = {}
for line in lst:
    if not line[0] in d:
        d[line[0]] = []
    if not line[1] in d:
        d[line[1]] = []
    d[line[0]].append(line[1])
    d[line[1]].append(line[0])

paths = []
for elem in d['start']:
    paths.append([False, 'start', elem])

res = []
while len(paths) > 0:
    tmp = []
    for path in paths:
        if path[-1] == 'end':
            continue
        directions = d[path[-1]]
        for direction in directions:
            if direction == 'start':
                continue
            elif direction[0].isupper() or direction not in path:
                x = copy(path)
                x.append(direction)
                if direction == 'end':
                    res.append(x)
            elif direction in path and path[0] == False:
                x = copy(path)
                x.append(direction)
                x[0] = True
            else:
                continue
            tmp.append(x)
    paths = tmp
print(len(res))
