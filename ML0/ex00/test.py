#!/usr/bin/env python

from matrix import Matrix, Vector
from typing import Optional, Any

def simple_vector(args: Any) -> Optional[Vector]:
    v = None
    try:
        v = Vector(args)
        vt = v.T()
        print(type(v))
        print(v.shape, end = ' ')
        print(v)
        print(vt.shape, end = ' ')
        print(vt, end = "\n\n")
    except Exception as e:
        print(e)
    return v

def simple_matrix(args: Any) -> Optional[Matrix]:
    v = None
    try:
        v = Matrix(args)
        vt = v.T()
        print(type(v))
        print(v.shape, end = ' ')
        print(v)
        print(vt.shape, end = ' ')
        print(vt, end = "\n\n")
    except Exception as e:
        print(e)
    return v

print("\033[33m \nVECTOR ERROR: \033[0m")
simple_vector(None)
simple_vector((1, 1))
simple_vector([[]])
simple_vector([[1, 2], [3, 4]])
simple_vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])

print("\033[33m \nVECTOR CORRECT: \033[0m")
simple_vector([[0]])
simple_vector([[1, 2, 3]])
simple_vector([[1], [2], [3]])
simple_vector(Vector([[1, 2]]))
simple_vector(Matrix([[1, 2]]))

print("\033[33m \nMATRIX ERROR: \033[0m")
simple_matrix(None)
simple_matrix((1, 0))
simple_matrix((-1, 1))
simple_matrix([[]])
simple_matrix([[], []])
simple_matrix([[0], []])
simple_matrix([[0], [None]])
simple_matrix([[1, 2], [3, 4, 5]])

print("\033[33m \nMATRIX CORRECT: \033[0m")
simple_matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
simple_matrix([[0., 2., 4.], [1., 3., 5.]])
simple_matrix(Vector([[1, 2]]))
simple_matrix(Matrix([[1, 2]]))

t1 = Matrix([[1, 2]]) + Vector([[2, 1]])
t2 = Vector([[1, 2]]) + Matrix([[2, 1]])
print(type(t1))
print(t1)
print(type(t2))
print(t2)


t1 = Matrix([[1, 2]]) - Vector([[2, 1]])
t2 = Vector([[1, 2]]) - Matrix([[2, 1]])
print(type(t1))
print(t1)
print(type(t2))
print(t2)