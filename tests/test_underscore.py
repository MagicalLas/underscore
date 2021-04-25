from underscore.underscore import _


def test_underscore_id_function():
    f = _

    assert f(1) == 1
    assert f("123") == "123"
