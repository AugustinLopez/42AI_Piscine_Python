#!/usr/bin/env python

from sys import argv

lst = [x.rstrip().split(',') for x in open(argv[1])][0]

state = [lst.count(str(x)) for x in range(9)]
print(state)
for c in range(256):
    x = state[0]
    for i in range(8):
        state[i] = state[i + 1]
    state[8] = x
    state[6] += x
print(sum(state))



    #res += calculus(int(argv[2])-elem, elem)


#for cycle in range(6):
#    add = 0
#    for i, x in enumerate(lst):
#        if x == 0:
#            lst[i] = 6
#            add += 1
#        else:
#            lst[i] -= 1
#    for i in range(add):
#        lst.append(8)
