from underscore.underscore import _


def test_underscore_id_function():
    f = _

    assert f(1) == 1
    assert f("123") == "123"


def test_underscore_add_number():
    f = _ + 10

    assert f(1) == 11


def test_underscore_get_property():
    class User(object):
        name: str

        def __init__(self):
            self.name = "LasWonho"

    user = User()

    f = _.name

    assert f(user) == "LasWonho"
