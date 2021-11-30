#!/usr/bin/env python
# https://stackoverflow.com/a/43399827

from ImageProcessor import ImageProcessor
import matplotlib
from sys import argv


if len(argv) > 1:
    imgp = ImageProcessor()
    with open('/proc/version') as fd:
        if fd.readline().find("WSL"):
            matplotlib.use('TKAgg')
    arr = imgp.load(argv[1])
    # print(arr)
    imgp.display(arr)
