#!/usr/bin/env python
"""
This is `kata01`: building a formatted string dynamically from a dictionary
"""

languages = {'Python': 'Guido van Rossum',
             'Ruby': 'Yukihiro Matsumoto',
             'PHP': 'Rasmus Lerdorf'}

for x in languages:
    print(x, "was created by", languages[x])
