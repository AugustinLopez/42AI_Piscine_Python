#!/usr/bin/env python

from random import sample


def generator(text, sep=" ", option=None):
    if not isinstance(text, str) \
            or not isinstance(sep, str) \
            or (option is not None and option != "ordered"
                and option != "unique" and option != "shuffle"):
        yield "ERROR"
        return
    final_array = text.split(sep)
    if (option == "shuffle"):
        ref_array = sample(range(len(final_array)), len(final_array))
        temp_array = []
        for i in range(len(final_array)):
            temp_array.append(final_array[ref_array[i]])
        final_array = temp_array
    elif (option == "ordered"):
        final_array.sort()
    elif (option == "unique"):
        final_array = list(dict.fromkeys(final_array))
    for elem in final_array:
        yield elem
