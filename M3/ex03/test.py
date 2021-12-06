#!/usr/bin/env python

import numpy as np
from ColorFilter import ColorFilter
from matplotlib import pyplot as plt
import matplotlib
from sys import argv

if len(argv) > 2:
    if len(argv) < 2:
        exit()
    try:
        with open('/proc/version') as fd:
            if fd.readline().find("WSL"):
                matplotlib.use('TKAgg')
    except Exception:
        pass
    array = plt.imread(argv[1])
    if np.shape(array)[2] == 4:
        print("RGBA")
    else:
        print("RGB")
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
    if argv[2].find('G') != -1:
        plt.imshow(cf.to_grayscale(array, 'm'))
        plt.show()
        plt.imshow(cf.to_grayscale(array, 'w', weights=[1.0, 0.0, 0.0]))
        plt.show()
        plt.imshow(cf.to_grayscale(array, 'w', weights=[0.0, 1.0, 0.0]))
        plt.show()
        plt.imshow(cf.to_grayscale(array, 'w', weights=[0.0, 0.0, 1.0]))
        plt.show()
        plt.imshow(cf.to_grayscale(cf.to_green(array), 'w',
                                   weights=[1.0, 0.0, 0.0]))
        plt.show()
        plt.imshow(cf.to_grayscale(cf.to_green(array), 'weight',
                                   weights=[0.0, 1.0, 0.0]))
        plt.show()
        plt.imshow(cf.to_grayscale(cf.celluloid(cf.invert(array)), 'm'))
        plt.show()
    plt.imshow(array)
    plt.show()
    exit()
