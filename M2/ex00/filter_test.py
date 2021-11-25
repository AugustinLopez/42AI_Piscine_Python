#!/usr/bin/env python

from ft_filter import ft_filter

function = lambda x: x + 1
iterable = [1, 2, 3]
print(ft_filter(function_to_apply = None, iterable = iterable))
try:
    print(list(ft_filter(function_to_apply = None, iterable = iterable)))
except Exception as e:
    print(e)
print(list(ft_filter(lambda x: x <= 1, [])))

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'o', 'z']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)