#!/usr/bin/env python

import numpy as np
from ColorFilter import ColorFilter
from matplotlib import pyplot as plt
from sys import argv

if len(argv) > 2:
    if len(argv) < 2:
        exit()
    array = plt.imread(argv[1])
    cf = ColorFilter()
    if argv[2].find('i') != -1:
        plt.imshow(cf.invert(array))
        plt.show()
    if argv[2].find('b') != -1:
        plt.imshow(cf.to_blue(array))
        plt.show()
    if argv[2].find('g') != -1:
        plt.imshow(cf.to_green(array))
        plt.show()
    if argv[2].find('r') != -1:
        plt.imshow(cf.to_red(array))
        plt.show()
    if argv[2].find('c') != -1:
        plt.imshow(cf.celluloid(array))
        plt.show()
    exit()    

    im = np.zeros(array.shape)
    im = np.dstack(array, im)
    plt.imshow(im)
    plt.show()
    exit()
    cf = ColorFilter()
    for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert, cf.celluloid]:
        array = plt.imread(argv[1])
        plt.imshow(f(array))
        plt.show()

    array = plt.imread(argv[1])
    im = cf.to_grayscale(array, "m")
    plt.imshow(im)
    plt.show()

    array = plt.imread(argv[1])
    im = cf.to_grayscale(array, "w", weights = [0.2126, 0.7152, 0.0722])
    plt.imshow(im)
    plt.show()

