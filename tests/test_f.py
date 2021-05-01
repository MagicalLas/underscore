from underscore.f import F
from underscore.underscore import _


def test_F_1():
    def add(a: int) -> int:
        return 12

    f = F(add)(_)

    assert f(2) == 12


def test_F_2():
    def add(a: int) -> int:
        return 12

    result = F(add)(10)

    assert result == 12


def test_F_print():
    f = F(print)(_)

    f("LasWonho")

