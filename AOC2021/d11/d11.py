#!/usr/bin/env python

from sys import argv

def controlled_increase(lst, tmp, y, x) -> int:
    if lst[y][x] == 10:
        return
    lst[y][x] += 1
    if lst[y][x] == 10:
        tmp.append((x, y))

def event1(lst, size_x, size_y):
    flash = []
    for y in range(size_y):
        for x in range(size_x):
            lst[y][x] += 1
            if lst[y][x] == 10:
                flash.append((x, y))
    return flash

def event2(lst, flash, size_x, size_y):
    res = 0
    while len(flash) > 0:
        res += len(flash)
        tmp = []
        for elem in flash:
            x = elem[0]
            y = elem[1]
            if x > 0:
                controlled_increase(lst, tmp, y, x - 1)
            if y > 0:
               controlled_increase(lst, tmp, y - 1, x)
            if x < size_x - 1:
                controlled_increase(lst, tmp, y, x + 1)
            if y < size_y - 1:
               controlled_increase(lst, tmp, y + 1, x)
            if x > 0 and y > 0:
                controlled_increase(lst, tmp, y - 1, x - 1)
            if x > 0 and y < size_y - 1:
                controlled_increase(lst, tmp, y + 1, x - 1)
            if x < size_x - 1 and y > 0:
                controlled_increase(lst, tmp, y - 1, x + 1)
            if x < size_x - 1 and y < size_y - 1:
                controlled_increase(lst, tmp, y + 1, x + 1)
        flash = tmp
    return res

def event3(lst, size_x, size_y):
    c = 0
    for y in range(size_y):
        for x in range(size_x):
            if lst[y][x] == 10:
                lst[y][x] = 0
                c +=1
    return c

lst = [[int(c) for c in n.rstrip()] for n in open(argv[1])]
size_x = len(lst[0])
size_y = len(lst)
res = 0
for step in range(1,10000):
    flash = event1(lst, size_x, size_y)
    res += event2(lst, flash, size_x, size_y)
    if step == 100:
        print(res)
    if (event3(lst, size_x, size_y) == size_x * size_y):
        print(step)
        break