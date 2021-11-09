#!/usr/bin/env python
"""
This is `kata04`: print formatted information
"""

test = [(0, 4, 132.42222, 10000, 12345.67),
        (10, 40, 132, 10000, 12345.67)]

for t in test:
    print("module_%02d ex_%02d: %.2f, %.2e, %.2e" % (t))
