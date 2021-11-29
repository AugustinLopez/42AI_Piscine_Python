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
            return 1.0 - array
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
            # Use Ellipsis to skip dimension 0 and 1: [R, G, B].
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
            return (0, 1, 0) * copy.deepcopy(array)
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
            return array - self.to_green(array) - self.to_blue(array)
        except Exception:
            return None

    def rescale(value, rounding, treshold):
        for i, elem in enumerate(treshold):
            if value <= elem:
                return rounding[i]
        return (0.0)

    def celluloid(self, array: np.ndarray) \
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
        rounding = np.linspace(0.0, 1.0, endpoint=True, num=4)
        treshold = np.linspace(0.25, 1.0, endpoint=True, num=4)
        for row in array:
            for pixel in row:
                for i in range(3): 
                    pixel[i] = ColorFilter.rescale(pixel[i], rounding, treshold)
        return array
    
    def to_grayscale(self, array, filter = "m", weights = [.299, .587, .114]) \
            -> Optional[np.ndarray]:
        if filter == "weighted" or filter == "w":
            for row in array:
                for pixel in row:
                    gray = sum(x*y for x, y in zip(weights, pixel))
                    for i in range(3): 
                        pixel[i] = gray
        elif filter == "mean" or filter == "m":
            for row in array:
                for pixel in row:
                    gray = (pixel[0] + pixel[1] +  pixel[2]) / 3
                    for i in range(3): 
                        pixel[i] = gray
        return array