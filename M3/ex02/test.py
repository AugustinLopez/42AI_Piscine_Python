#!/usr/bin/env python


import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
arr1 = np.arange(0, 25).reshape(5, 5)
arrA = spb.crop(arr1, (3, 1), (1, 0))
print(arr1)
print(arrA)
print()

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
arrB = spb.thin(arr2, 3, 0)
print(arr2)
print(arrB)
print()

arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
arrC = spb.thin(arr3, 3, 1)
print(arr3)
print(arrC)
print()

arr4 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
arrD = spb.juxtapose(arr4, 3, 1)
print(arr4)
print(arrD)
print()

arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arrE = spb.juxtapose(arr5, 2, 0)
print(arr5)
print(arrE)
print()

arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arrF = spb.mosaic(arr5, (2, 3))
print(arr6)
print(arrF)
print()

not_numpy_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spb.crop(not_numpy_arr, (1, 2)))
print(spb.juxtapose(arr4, -2, 0))
print(spb.mosaic(arr4, (1, 2, 3)))
