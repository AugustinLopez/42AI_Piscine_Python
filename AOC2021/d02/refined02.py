#!/usr/bin/env python

from sys import argv


lst = [str(x).split(' ') for x in open(argv[1])]
lst = [[x[0], int(y)] for x, y in lst]
aim = horizon = depth = 0
for x, y in lst:
      if x == 'f':
            horizon += y
            depth += aim * y
      else:
            aim += y if x == 'd' else -y
print(aim * horizon)
print(depth * horizon)
