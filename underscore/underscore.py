from typing import TypeVar, Generic, List, Any, Mapping


def is_callable(x):
    return hasattr(x, '__call__')


T = TypeVar('T')


class Lambda(Generic[T]):
    def __init__(self, type_value: type):
        self.type_value = type_value
        self.type_instance: T = type_value()
        self._operations: List[str] = []

    def add_operation(self, operation: str):
        self._operations.append(operation)

    def is_method_call(self, attr_name: str) -> bool:
        return callable(eval(f"self.type_instance.{attr_name}"))

    def evaluation(self, actual_value: T) -> Any:
        middle_value = actual_value
        for op in self._operations:
            middle_value = eval(f"middle_value{op}")
        return middle_value

    def method_call(self, method_name: str, args: List[Any], kwargs: Mapping[str, Any]):
        self.add_operation(f".{method_name}(*{args}, **{kwargs})")

    def get_item(self, item):
        self.add_operation(f"[{item}]")


class Underscore:
    def __init__(self, _is_use_lambda: bool = False, _lambda=None):
        self._is_use_lambda = _is_use_lambda
        self._lambda: Lambda[T] = _lambda

    def __call__(self, value: T):
        if self._is_use_lambda:
            return self._lambda.evaluation(value)
        return value

    def __getitem__(self, _type: T) -> T:
        if self._is_use_lambda:
            self._lambda.get_item(_type)
            return Underscore(True, self._lambda)
        return Underscore(True, Lambda[T](_type))

    def __add__(self, number):
        def wrapper(value):
            return value + number

        return wrapper

    def __getattr__(self, attr_name: str):
        if self._is_use_lambda and self._lambda.is_method_call(attr_name):
            def wrapper_for_method(*args, **kwargs):
                self._lambda.method_call(attr_name, args, kwargs)
                return Underscore(self._is_use_lambda, self._lambda)

            return wrapper_for_method

        def wrapper(value: T):
            return eval(f"value.{attr_name}")

        return wrapper


_ = Underscore()
