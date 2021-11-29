import numpy as np
import warnings
from typing import Optional, List, Union, Tuple, Iterable


class NumPyCreator():
    def __init__(self):
        pass

    def from_list(self, lst: List[Union[float, int, List, Tuple]]) \
            -> Optional[np.ndarray]:
        if not isinstance(lst, list):
            return None
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                return np.array(lst)
        except Exception:
            return None

    def from_tuple(self, tpl: Tuple[Union[float, int, List, Tuple]]) \
            -> Optional[np.ndarray]:
        if not isinstance(tpl, tuple):
            return None
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                return np.array(tpl)
        except Exception:
            return None

    def from_iterable(self, itr: Iterable) -> Optional[np.ndarray]:
        try:
            _ = iter(itr)
            return np.array(itr)
        except Exception:
            return None

    def from_shape(self, shape: Tuple[int],
                   value: Union[int, float] = 0) \
            -> Optional[np.ndarray]:
        if not isinstance(shape, tuple):
            return None
        if not (isinstance(value, int) or isinstance(value, float)):
            return None
        try:
            return np.full(shape, value)
        except Exception:
            return None

    def random(self, shape: Tuple[int]) -> Optional[np.ndarray]:
        try:
            return np.random.rand(shape[0], shape[1])
        except Exception:
            return None

    def identity(self, n: int) -> Optional[np.ndarray]:
        if not (isinstance(n, int)):
            return None
        try:
            return np.identity(n)
        except Exception:
            return None
