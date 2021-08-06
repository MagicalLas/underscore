from typing import TypeVar, Protocol

A = TypeVar("A", covariant=True)


class F(Protocol[A]):
    ...
