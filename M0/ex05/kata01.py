#!/usr/bin/env python
"""
This is `kata01`: building a formatted string dynamically from a dictionary
"""

test = [{'Python': 'Guido van Rossum',
         'Ruby': 'Yukihiro Matsumoto',
         'PHP': 'Rasmus Lerdorf'},
        {},
        {'Python': 'Guido'}]

for languages in test:
    print()
    for x in languages:
        print(x, "was created by", languages[x])
