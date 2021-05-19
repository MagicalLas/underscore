from typing import Callable

from underscore.underscore import Underscore


class FWrapper(Callable):
    def __init__(self, function: Callable):
        print(function)
        self.function = function

    def __call__(self, *args, **kwargs):
        if isinstance(self.function, FWrapper):
            return self.function(*args, **kwargs)

        if len(args) < 1:
            return self.function(*args, **kwargs)

        if not isinstance(args[0], Underscore):
            return self.function(*args, **kwargs)

        def wrapper2(*args, **kwargs):
            return self.function(*args, **kwargs)

        return wrapper2


def F(function: Callable) -> Callable:
    return FWrapper(function)
