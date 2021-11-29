#!/usr/bin/env python

from NumPyCreator import NumPyCreator


def example_list():
    npc = NumPyCreator()
    print("\033[33m FROM_LIST:\033[0m")
    elem = npc.from_list([[1, 2, 3], [6, 3, 4]])
    print(elem)
    print()
    elem = npc.from_list([[1, 2, 3], [6, 4]])
    print(elem)
    print()
    elem = npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]])
    print(elem)
    print()
    elem = npc.from_list(((1, 2), (3, 4)))
    print(elem)
    print()
    elem = npc.from_list([[], []])
    print(elem)
    print()
    elem = npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6]])
    print(elem)
    print()


def example_tuple():
    npc = NumPyCreator()
    print("\033[33m FROM_TUPLE:\033[0m")
    elem = npc.from_tuple(("a", "b", "c"))
    print(elem)
    print()
    elem = npc.from_tuple([[1, 2, 3], [6, 3, 4]])
    print(elem)
    print()
    elem = npc.from_tuple(([1, 2, 3], [6, 3, 4]))
    print(elem)
    print()
    elem = npc.from_tuple(((1, 2, 3), (6, 3, 4)))
    print(elem)
    print()


def example_rest():
    npc = NumPyCreator()
    print("\033[33m OTHER EXAMPLES:\033[0m")
    elem = npc.from_iterable(range(5))
    print(elem)
    print()
    elem = npc.from_shape((3, 5))
    print(elem)
    print()
    elem = npc.from_shape((0, 0))
    print(elem)
    print()
    elem = npc.random((3, 5))
    print(elem)
    print()
    elem = npc.identity(4)
    print(elem)
    print()


def example_error():
    npc = NumPyCreator()
    print(npc.from_list("toto"))
    print(npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6, 7]]))
    print(npc.from_tuple(3.2))
    print(npc.from_tuple(((1, 5, 8), (7, 5))))
    print(npc.from_shape((-1,  -1)))
    print(npc.from_shape((1, 5, 8), (7, 5)))
    print(npc.identity(-1))


example_list()
example_tuple()
example_rest()
example_error()
