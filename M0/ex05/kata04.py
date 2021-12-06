#!/usr/bin/env python
"""
This is `kata04`: print formatted information
"""

test = [(0, 4, 132.42222, 10000, 12345.67),
        (15, 15, 15.155, 1554, 1.515) ]

for t in test:
    print("module_%02d ex_%02d: %.2f, %.2e, %.2e" % (t))
