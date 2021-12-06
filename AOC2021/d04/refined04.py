#!/usr/bin/env python

from sys import argv
import numpy as np

head, *body = [x.rstrip() for x in open(argv[1])]
announce = map(int, head.split(','))
players = np.reshape(np.loadtxt(body, int), (-1,5,5))
a = -1
b = -1
for n in announce:
    players[players == n] = -1
    bingo = (players == -1)
    win = np.any((np.all(bingo, 1) | bingo.all(2)), 1)
    if win.any():
        b = (players * ~bingo)[win].sum() * n
        a = a if a != -1 else b
        players = players[~win]
print("A:{}\nB:{}".format(a,b))