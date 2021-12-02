#!/usr/bin/env python

from sys import argv


with open(argv[1]) as fd:
    val = int(fd.readline())
    i = 0
    for line in fd.readlines():
        x = int(line)
        if x > val:
            i += 1
        val = x
    print(i)
