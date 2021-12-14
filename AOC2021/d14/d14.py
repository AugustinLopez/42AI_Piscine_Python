#!/usr/bin/env python3

from sys import argv
from copy import copy, deepcopy
from collections import Counter, defaultdict

head, space, *input = [line.rstrip() for line in open(argv[1])]
head2 = copy(head)
input = [y.split(' -> ') for y in input]

for step in range(10):
    part = [head[i:i+2] for i in range(len(head) - 1)]
    tmp = [head[i:i+2] for i in range(len(head) - 1)]
    for r, p in enumerate(part):
        for i in input:
            if p in i[0]:
                tmp[r] = p[0] + i[1]
                break
    head = ''.join(tmp) + head[-1]
counter = Counter(head)
print(max(counter.values()) - min(counter.values()))

my_dict = defaultdict(lambda: 0)
part = [head2[i:i+2] for i in range(len(head2) - 1)]
for p in part:
    my_dict[p] += 1

for step in range(40):
    tmp = deepcopy(my_dict)
    for k in my_dict.keys():
        for i in input:
            if k in i[0]:
                tmp[k[0] + i[1]] += my_dict[k]
                tmp[i[1] + k[1]] += my_dict[k]
                tmp[k] -= my_dict[k]
                break
    my_dict = tmp
letters = list({l for word in my_dict.keys() for l in word})
my_res = {l: 0 for l in letters}
for r in my_res.keys():
    for i, k in enumerate(my_dict.keys()):
        if r == k[1]:
            my_res[r] += my_dict[k]
my_res[head2[0]] += 1
print(max(my_res.values()) - min(my_res.values()))


