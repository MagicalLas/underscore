from typing import Callable, Any

from underscore.underscore import Underscore


def F(function: Callable) -> Callable:
    def wrapper(any: Any):
        if isinstance(any, Underscore):
            def wrapper2(*args):
                return function(*args)
            return wrapper2
        return function(any)
    return wrapper
