from typing import Iterable, Callable, Optional, Any

def ft_reduce2(function_to_apply, list_of_inputs):
	listing = list(list_of_inputs)
	result = listing[0]
	for elem in listing[1:]:
		result = function_to_apply(result, elem)
	return (result)

def ft_reduce(function_to_apply: Optional[Callable[[Any, Any], Any]],
           iterable: Iterable) -> Any:
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("Expected callable. Got " + str(type(function_to_apply)))
    try:
        _ = iter(iterable)
    except TypeError:
        raise TypeError("Expected iterable. Got " + str(type(iterable)))
    try:
        for i, _ in enumerate(iterable, 0):
            if i == 0:
                result = iterable[0]
                continue
            result = function_to_apply(result, iterable[i])
            # yield result
    except Exception:
        return None
    return result
