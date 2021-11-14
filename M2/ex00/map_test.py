#!/usr/bin/env python

from ft_map import ft_map

function = lambda x: x + 1
iterable = [1, 2, 3]
print(ft_map(function_to_apply = None, iterable = iterable))
try:
    print(list(ft_map(function_to_apply = None, iterable = iterable)))
except Exception as e:
    print(e)
print(list(ft_map(lambda x: x + 2, [])))
print(list(ft_map(lambda x: x + 2, [1])))
print(list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
def to_upper_case(s):
    return str(s).upper()

def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

list_numbers = [1, 2, 3, 4]
map_iterator = map(lambda x: x * 2, list_numbers)
print(type(map_iterator))
print_iterator(map_iterator)

map_iterator = ft_map(lambda x: x * 2, list_numbers)
print(type(map_iterator))
print_iterator(map_iterator)

txt = 'abc'
map_iterator = map(to_upper_case, txt)
print(type(map_iterator))
print_iterator(map_iterator)

map_iterator = ft_map(to_upper_case, txt)
print(type(map_iterator))
print_iterator(map_iterator)

x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(list(ft_map(lambda t: t + 1, x)))
