#!/usr/bin/env python
"""
This is `kata02`: building a formatted date from a tuple
"""

import datetime

t = (3, 30, 2019, 9, 25)

d = datetime.datetime(t[2], t[3], t[4], t[0], t[1])
print(d.strftime("%m/%d/%Y %H:%M"))
