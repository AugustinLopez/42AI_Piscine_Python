#!/usr/bin/env python

from sys import argv
from os import system
from time import sleep

def recursive(res, lst, size_i, size_j):
    ret = []
    total = len(res)
    print(res)
    d = {i[3]: 1 for i in res}
    print(d)

    tmp = res
    while len(tmp) > 0:
        print()
        ret = []
        for elem in tmp:
            i = elem[0]
            j = elem[1]
            val = elem[2]
            origin = elem[3]
            if j > 0:
                if lst[i][j-1][0] > val and lst[i][j-1][0] <9 and lst[i][j-1][1] == 0:
                    ret.append((i, j-1, lst[i][j-1][0], origin))
                    d[origin]+=1
                    lst[i][j-1][1] = 32 if lst[i][j-1][1] == 0 else 33
            if i > 0:
                if lst[i-1][j][0] > val and lst[i-1][j][0] <9  and lst[i-1][j][1] == 0:
                    ret.append((i-1, j, lst[i-1][j][0], origin))
                    d[origin]+=1
                    lst[i-1][j][1]= 32 if lst[i-1][j][1]== 0 else 33
            if j < size_j - 1:
                if lst[i][j+1][0]  > val and lst[i][j+1][0]  <9  and lst[i][j+1][1] == 0:
                    ret.append((i, j+1, lst[i][j+1][0], origin))
                    d[origin]+=1
                    lst[i][j+1][1] = 32 if lst[i][j+1][1]== 0 else 33
            if i < size_i - 1:
                if lst[i+1][j][0] > val and lst[i+1][j][0] <9  and lst[i+1][j][1] == 0:
                    ret.append((i+1, j, lst[i+1][j][0], origin))
                    d[origin]+=1
                    lst[i+1][j][1] = 32 if lst[i+1][j][1] == 0 else 33
        for i in range(size_i):
            for j in range(size_j):
                if lst[i][j][1] != 0:
                    print("\x1b[{}m".format(lst[i][j][1]), end='')
                    if lst[i][j][1] ==32:
                        lst[i][j][1] = 34
                else:
                    print("\x1b[30m", end='')
                print("{}".format(lst[i][j][0]), end = '')
                print("\x1b[0m", end='')
            print()
        tmp = ret
        total += len(ret)
    my_keys = sorted(d, key=d.get, reverse=True)[:3]
    final = d[my_keys[0]]
    for i in my_keys[1:]:
        final *= d[i]
    print(final)


lst = []
for x in [y.rstrip() for y in open(argv[1])]:
    lst.append([[int(c),0, -1] for c in x])
size_j = len(lst[0])
size_i = len(lst)
res = []
final = 0

for i in range(size_i):
    for j in range(size_j):
        refuse = False
        if j > 0:
            if lst[i][j][0] >= lst[i][j - 1][0]:
                refuse = True
        if i > 0:
            if lst[i][j][0] >= lst[i - 1][j][0]:
                refuse = True
        if j < size_j - 1:
            if lst[i][j][0] >= lst[i][j + 1][0]:
                refuse = True
        if i < size_i - 1:
            if lst[i][j][0] >= lst[i + 1][j][0]:
                refuse = True
        if refuse == False:
            res.append((i, j, lst[i][j][0], (i,j)))
            lst[i][j][1]=33
            lst[i][j][2]=(i, j)
            final+= lst[i][j][0]+1
            print("\x1b[32m", end='')
            print("{}".format(lst[i][j][0]), end = ' ')
            print("\x1b[0m", end='')
        else:
            print("{}".format(lst[i][j][0]), end = ' ')
    print()

recursive(res, lst, size_i, size_j)
print(final)