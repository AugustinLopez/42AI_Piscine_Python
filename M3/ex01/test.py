#!/usr/bin/env python
# https://stackoverflow.com/a/43399827

from ImageProcessor import ImageProcessor
import matplotlib
import platform
from sys import argv


if len(argv) > 1:
    imgp = ImageProcessor()
    if platform.system() == 'Windows':
        matplotlib.use('GTK3Agg')
    arr = imgp.load(argv[1])
    print(arr)
    imgp.display(arr)
