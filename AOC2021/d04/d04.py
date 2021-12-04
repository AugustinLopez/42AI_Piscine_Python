#!/usr/bin/env python

from sys import argv
import numpy as np
from copy import deepcopy

def eliminate(arr, p):
    x = deepcopy(arr[p])
    for i in range(5):
        for j in range(5):
            arr[p][i][j] = -2
    return x

def winner_check(arr):
    for x, p in enumerate(arr):
        for i in range(5):
            c = 0
            for j in range(5):
                if p[i][j] == -1:
                    c +=1
            if c == 5:
                return p,x
            c = 0
            for j in range(5):
                if p[j][i] == -1:
                    c +=1
            if c == 5:
                return p,x
    return None


lst = [x.rstrip() for x in open(argv[1])]
announce = lst.pop(0).split(',')
lst.pop(0)
announce = [int(i) for i in announce]
player = [[]]
p = 0
n = 3
for elem in lst:
    tmp = [int(elem[i:i+n]) for i in range(0, len(elem), n)]
    if len(tmp) > 0:
        player[p].append(tmp)
    else:
        player.append([])
        p += 1
p += 1
player = np.array(player)

for a in announce[:5]:
    for i in range(p):
        for j in range(5):
            for k in range(5):
                if player[i][j][k] == a:
                    player[i][j][k] = -1
tmp = winner_check(player)
b = 0
if tmp is not None:
    b = a
    x = player[tmp[1]] + 0
    for i in range(5):
        for j in range(5):
            player[tmp[1]][i][j] = -2
    tmp = None
for a in announce[5:]:
    for i in range(p):
        for j in range(5):
            for k in range(5):
                if player[i][j][k] == a:
                    player[i][j][k] = -1
    tmp = winner_check(player)
    while tmp is not None:
        x = player[tmp[1]] + 0
        for i in range(5):
            for j in range(5):
                player[tmp[1]][i][j] = -2
        b = a
        tmp = winner_check(player)
res = x
print(player)
c = 0
for i in range(5):
    for j in range(5):
        if res[i][j] != -1:
            c+=res[i][j]
print(c * b)
