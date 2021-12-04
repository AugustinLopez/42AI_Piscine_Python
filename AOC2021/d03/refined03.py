#!/usr/bin/env python


from sys import argv
from collections import Counter

lst = [str(x).rstrip() for x in open(argv[1])]
theta = ['1'] * len(lst[0])
epsilon = ['0'] * len(lst[0])
oxygen = lst
co2 = lst
for i in range(len(lst[0])):
      c = sum(int(x[i]) for x in lst) - len(lst) / 2.0
      if c > 0:
            theta[i] = '0'
            epsilon[i] = '1'
      if len(oxygen) > 1:
            c = Counter([x[i] for x in oxygen])
            oxygen = [x for x in oxygen if x[i] == str(0 + (c['1'] >= c['0']))]
      if len(co2) > 1:
            c = Counter([x[i] for x in co2])
            co2 = [x for x in co2 if x[i] == str(0 + (not c['1'] >= c['0']))]
print(int("".join(theta), 2) * int("".join(epsilon), 2))
print(int(oxygen[0], 2) * int(co2[0], 2))