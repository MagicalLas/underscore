from __future__ import annotations

from collections import Container
from typing import Generic, TypeVar, Union, Any

from underscore.core.applicative import Applicative
from underscore.core.f import F
from underscore.core.function import Function

A1 = TypeVar("A1")
B1 = TypeVar("B1")

A = TypeVar("A")
B = TypeVar("B")

A2 = TypeVar("A2")


class Either(Generic[A1, B1], F, Applicative):

    @staticmethod
    def ap(ffa: F[Function[A, B]]) -> Function[F[A], F[B]]:
        ...

    @staticmethod
    def pure(a: A) -> Left[A]:
        ...

    @staticmethod
    def map(fa: F[A]) -> Function[Function[A, B], F[B]]:
        def mf(f: Function[A, B]) -> Left[B]:
            ffa: Left[Function[A, B]] = Either.pure(f)
            ap: Function[Left[A], Left[B]] = Either.ap(ffa)
            return ap(fa)

        return mf


class Left(Generic[A], Either[A, Any], F):
    ...


a: Applicative = Either.pure("")
