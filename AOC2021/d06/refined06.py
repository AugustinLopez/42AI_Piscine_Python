#!/usr/bin/env python

from sys import argv

# lst = [int(x) for x in open(argv[1]).readline().split(',')]
#state = [lst.count(x) for x in range(9)]

lst = [*map(int, open(argv[1]).readline().split(','))]
state = [*map(lst.count, range(9))]

for c in range(int(argv[2])):
    state = state[1:] + state[:1]
    state[6] += state[-1]
print(sum(state))