#!/usr/bin/env python
"""
This is `kata02`: building a formatted date from a tuple
"""

import datetime

test = [(3, 30, 2019, 9, 25)]

for t in test:
    print("%02d/%02d/%04d %02d:%02d" % (t[3], t[4], t[2], t[0], t[1]))
    # d = datetime.datetime(t[2], t[3], t[4], t[0], t[1])
    # print(d.strftime("%m/%d/%Y %H:%M"))
