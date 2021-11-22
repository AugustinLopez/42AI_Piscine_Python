import numpy as np


class NumPyCreator():
	def __init__(self):
		pass

	def from_list(self, lst, dt = None):
		return np.array(lst, dtype = dt)

	def from_tuple(self, tpl, dt = None):
		return np.array(tpl, dtype = dt)

	def from_iterable(self, itr, dt = None):
		return np.array(itr, dtype = dt)

	def from_shape(self, shape, value = 0, dt = None):
		return np.full(shape, value, dtype = dt)

	def random(self, shape):
		return np.random.rand(shape[0], shape[1])

	def identity(self, n, dt = None):
		return np.identity(n, dtype = dt)