from typing import Iterable, Callable, Optional, Any


def ft_map(function_to_apply: Optional[Callable[[Any], Any]],
           iterable: Iterable) -> Optional[Iterable]:
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("Expected callable. Got "
                        + str(type(function_to_apply)))
    try:
        _ = iter(iterable)
    except TypeError:
        raise TypeError("Expected iterable. Got "
                        + str(type(iterable))) from None
    try:
        for elem in iterable:
            yield function_to_apply(elem)
    except Exception:
        return None
