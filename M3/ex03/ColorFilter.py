import numpy as np
from typing import Optional
import copy


class ColorFilter():
    def __init__(self):
        pass

    def invert(self, array: np.ndarray) -> Optional[np.ndarray]:
        """
        Inverts the color of the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            return (1, 1, 1) - array[...,:3]
        except Exception:
            return None

    def to_blue(self, array: np.ndarray) \
            -> Optional[np.ndarray]:
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            return np.dstack((np.zeros(np.shape(array[..., 2])),
                              np.zeros(np.shape(array[..., 2])),
                              array[..., 2]))
        except Exception:
            return None

    def to_green(self, array: np.ndarray) \
            -> Optional[np.ndarray]:
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            return (0, 1, 0) * copy.deepcopy(array[...,:3])
        except Exception:
            return None

    def to_red(self, array: np.ndarray) \
            -> Optional[np.ndarray]:
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            return array[...,:3] - self.to_green(array) - self.to_blue(array)
        except Exception:
            return None

    def celluloid(self, array: np.ndarray) \
            -> Optional[np.ndarray]:
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception
        """
        tmp = array[..., :3].copy()
        for i in range(3):
            x = tmp[..., i]
            rounding = np.linspace(x.min(), x.max(), endpoint=True, num=4)
            treshold = np.linspace(x.min(), x.max(), endpoint=True, num=5)
            for r, t1, t2 in zip(rounding, treshold[:-1], treshold[1:]):
                x[(x > t1) & (x <= t2)] = r
        return tmp

    def to_grayscale(self, array, filter = "m", weights = [.299, .587, .114]) \
            -> Optional[np.ndarray]: # need kwargs instead of weights
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        if filter == "weight" or filter == "w":
            x = np.tile(array[..., :3], 1) * weights
            x = np.sum(x, axis=2)
            return np.dstack((x,x,x))
        elif filter == "mean" or filter == "m":
            x = np.sum(array[..., :3], axis=2) / 3
            return np.dstack((x,x,x))
        return array