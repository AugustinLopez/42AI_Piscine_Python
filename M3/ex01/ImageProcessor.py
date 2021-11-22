#!/usr/bin/env python
# https://stackoverflow.com/a/43399827
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib
import os

class ImageProcessor():
	def __init__(self):
		pass

	def load(self, path: str):
		if os.path.exists(path) and os.path.isfile(path):
			img = mpimg.imread(path)
			print("Loading image of dimension {} x {}"
				.format(img.shape[0], img.shape[1]))
			return img
		return None
	
	def display(self, array: np.array):
		if array is None:
			return
		plt.imshow(array)
		plt.show()

imgp = ImageProcessor()
matplotlib.use('GTK3Agg')
arr =imgp.load("42AI.png")
imgp.display(arr)