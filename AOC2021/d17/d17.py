#!/usr/bin/env python3
#https://www.reddit.com/r/adventofcode/comments/rily4v/2021_day_17_part_2_never_brute_force_when_you_can/

from sys import argv

def p1(pos_y):
    y = -pos_y[0] - 1
    height = y * (y + 1) // 2
    print("{}".format(height))

txt = open(argv[1]).readline()[13:]
target = txt.split(', ')
pos_x = list(map(int, target[0][2:].split('..')))
pos_y = list(map(int, target[1][2:].split('..')))
p1(pos_y)
C=0
for y in range(pos_y[0], 1-pos_y[0]):
    for x in range(pos_x[1]+1):
        v=u=0
        for t in range(500):
            v+=y-t
            u+=max(x-t, 0)
            if pos_x[0]<=u<=pos_x[1] \
            and pos_y[0]<=v<=pos_y[1]:
                C+=1
                break
print(C)