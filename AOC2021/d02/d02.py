#!/usr/bin/env python

from sys import argv


lst = [str(x).rstrip().split(' ') for x in open(argv[1])]
a = 0
h = 0
d = 0
for elem in lst:
      if elem[0][0] == 'f':
            h += int(elem[1])
            d += a * int(elem[1])
      elif elem[0][0] == 'd':
            a += int(elem[1])
      elif elem[0][0] == 'u':
            a -= int(elem[1])
print(a*h)
print(d*h)
