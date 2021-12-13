#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

folds=[]
coordinates = {}
switch = False
for line in open(argv[1]):
    if line == "\n":
        switch = True
    elif switch == False:
        tmp = line.rstrip().split(',')
        coordinates[(int(tmp[0]), int(tmp[1]))] = 1
    else:
        tmp = line.rstrip().split('=')
        folds.append([tmp[0][-1], int(tmp[1])])
for i, fold in enumerate(folds):
    xy = fold[1]
    tmp = defaultdict(lambda: 0)
    if fold[0] == 'x':
        for coor in coordinates.keys():
            if coor[0] < xy:
                tmp[coor] = coordinates[coor]
            elif coor[0] > xy:
                tmp[(xy - (coor[0] - xy), coor[1])] += 1
    else:
        for coor in coordinates.keys():
            if coor[1] < xy:
                tmp[coor] = coordinates[coor]
            elif coor[1] > xy:
                tmp[(coor[0], xy - (coor[1] - xy))] += 1
    coordinates = tmp
    if i == 0:
        print(len(coordinates))

tmp = [[k[0] for k in coordinates.keys()], [k[1] for k in coordinates.keys()]]
max_x = max(tmp[0])
max_y = max(tmp[1])
for y in range(max_y  + 1):
    for x in range(max_x + 1):
        if (x, y) in coordinates:
            print('▮', end='')
        else:
            print(' ', end='')
    print()
print()