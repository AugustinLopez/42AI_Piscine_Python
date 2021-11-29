# https://stackoverflow.com/a/43399827

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os


class ImageProcessor():
    def __init__(self):
        pass

    def load(self, path: str):
        try:
            img = mpimg.imread(path)
            print("Loading image of dimension {} x {}"
                  .format(img.shape[0], img.shape[1]))
            return img
        except FileNotFoundError as e:
            raise FileNotFoundError(e) from None
        except OSError as e:
            raise OSError(e) from None
        except Exception as e:
            raise AssertionError(e) from None
        return None

    def display(self, array: np.ndarray):
        if array is None:
            return
        try:
            plt.imshow(array)
            plt.show()
        except Exception:
            return
