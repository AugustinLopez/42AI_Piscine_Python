#!/usr/bin/env python3

from sys import argv
from copy import deepcopy, copy

def select_path(paths):
    m = -1
    index = -1
    for i, p in enumerate(paths):
        if p[2] == -1:
            pass
        if m == -1 or p[2] < m:
            m = p[2]
            index = i
    return index

lst = [list(map(int, line.rstrip())) for line in open(argv[1])]

tmp = deepcopy(lst)
p2 = 5
for _ in range(p2 - 1):
    tmp = [[i % 9 + 1 for i in line] for line in tmp]
    lst += tmp
for t in lst:
    tmp = copy(t)
    for _ in range(p2 - 1):
        tmp = [i % 9 + 1 for i in tmp]
        t += tmp
lst[0][0] = 0
len_y = len(lst)
len_x = len(lst[0])
paths = [(0,0,0)]
end = False

while True:
    index = select_path(paths)
    path = paths[index]
    y = path[0]
    x = path[1]
    l = path[2]
    if x > 0:
        a = y
        b = x - 1
        if lst[a][b] > 0:
            paths.append((a, b, l + lst[a][b]))
        lst[a][b] = 0
    if y > 0:
        a = y - 1
        b = x
        if lst[a][b] > 0:
            paths.append((a, b, l + lst[a][b]))
        lst[a][b] = 0
    if x < len_x - 1:
        a = y
        b = x + 1
        if a == len_y - 1 and b == len_x - 1:
            print(l + lst[a][b])
            break
        if lst[a][b] > 0:
            paths.append((a, b, l + lst[a][b]))
        lst[a][b] = 0
    if y < len_y - 1:
        a = y + 1
        b = x
        if a == len_y - 1 and b == len_x - 1:
            print(l + lst[a][b])
            break
        if lst[a][b] > 0:
            paths.append((a, b, l + lst[a][b]))
        lst[a][b] = 0
    del paths[index]