import numpy as np
from typing import Tuple, Optional


class ScrapBooker():
    def __init__(self):
        pass

    def crop(self, array: np.ndarray,
             dimension: Tuple[int, int],
             position: Tuple[int, int] = (0, 0)) \
            -> Optional[np.ndarray]:
        """
        Crops the image as a rectangle via dim arguments
        (being the new height and width oof the image)
        from the coordinates given by position arguments.
        Args:
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Returns:
        new_arr: the cropped numpy.ndarray.
        None otherwise (combinaison of parameters not compatible).
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(dimension, Tuple) \
                or not isinstance(position, Tuple):
            return None
        if len(dimension) != 2 or len(position) != 2:
            return None
        if not isinstance(dimension[0], int) \
                or not isinstance(dimension[1], int):
            return None
        if not isinstance(position[0], int) \
                or not isinstance(position[1], int):
            return None
        if not isinstance(array, np.ndarray):
            return None
        try:
            x = position[0]
            y = position[1]
            w = dimension[0]
            h = dimension[1]
            original_w = array.shape[0]
            original_h = array.shape[1]
            if x + w > original_w or y + h > original_h or x < 0 or y < 0:
                raise ValueError("Crop outside range")
            return array[x:x+w, y:y+h]
        except Exception:
            return None

    def thin(self, array: np.ndarray, n: int, axis: int) \
            -> Optional[np.ndarray]:
        """
        Deletes every n-th line pixels along the specified axis
        (0: vertical, 1: horizontal)
        Args:
        array: numpy.ndarray.
        n: non null positive integer lower than the number of
        row/column of the array (depending on axis value).
        axis: integer of value 0 or 1.
        Returns:
        new_arr: thined numpy.ndarray.
        None otherwise (combinaison of parameters not compatible).
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(n, int) and not isinstance(axis, int):
            return None
        if n <= 0 or axis < 0 or axis > 1:
            return None
        if not isinstance(array, np.ndarray):
            return None
        try:
            return np.delete(array, slice(n - 1, None, n), not axis)
        except Exception:
            return None

    def juxtapose(self, array: np.ndarray, n: int, axis: int) \
            -> Optional[np.ndarray]:
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        new_arr: juxtaposed numpy.ndarray.
        None otherwise (combinaison of parameters not compatible).
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(n, int) and not isinstance(axis, int):
            return None
        if n <= 0 or axis < 0 or axis > 1:
            return None
        if not isinstance(array, np.ndarray):
            return None
        try:
            if not axis:
                return np.tile(array, (n, 1))
            return np.tile(array, (1, n))
        except Exception:
            return None

    def mosaic(self, array: np.ndarray, dimension: Tuple[int, int]) \
            -> Optional[np.ndarray]:
        """
        Makes a grid with multiple copies of the array.
        The dim argument specifies the number of repetition
        along each dimensions.
        Args:
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Returns:
        new_arr: mosaic numpy.ndarray.
        None otherwise (combinaison of parameters not compatible).
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(dimension, Tuple):
            return None
        if len(dimension) != 2:
            return None
        if not isinstance(dimension[0], int) \
                or not isinstance(dimension[1], int):
            return None
        if not isinstance(array, np.ndarray):
            return None
        try:
            return np.tile(array, dimension)
        except Exception:
            return None
