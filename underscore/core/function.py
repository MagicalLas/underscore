from typing import TypeVar, Protocol, Container, Callable

A = TypeVar("A", contravariant=True)
B = TypeVar("B", covariant=True)


class Function(Protocol[A, B]):
    def __call__(self, a: A, /) -> B: ...
