from __future__ import annotations

from typing import TypeVar, Protocol

from underscore.core.f import F
from underscore.core.function import Function

A = TypeVar("A")
B = TypeVar("B")


class Functor(Protocol):
    @staticmethod
    def map(fa: F[A]) -> Function[Function[A, B], F[B]]: ...
