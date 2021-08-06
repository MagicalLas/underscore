from __future__ import annotations

from typing import TypeVar, Protocol

from underscore.core.f import F
from underscore.core.function import Function
from underscore.core.functor import Functor

A = TypeVar("A")
B = TypeVar("B")


class Applicative(Protocol, Functor):
    @staticmethod
    def ap(ffa: F[Function[A, B]]) -> Function[F[A], F[B]]:
        ...

    @staticmethod
    def pure(a: A) -> F[A]:
        ...

    @staticmethod
    def map(fa: F[A]) -> Function[Function[A, B], F[B]]:
        def mf(f: Function[A, B]) -> F[B]:
            return Applicative.ap(Applicative.pure(f))(fa)

        return mf
