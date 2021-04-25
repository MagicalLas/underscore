from underscore.underscore import _


class User(object):
    name: str

    def __init__(self):
        self.name = "LasWonho"


def test_underscore_id_function():
    f = _

    assert f(1) == 1
    assert f("123") == "123"


def test_underscore_add_number():
    f = _ + 10

    assert f(1) == 11


def test_underscore_get_property():
    user = User()

    f = _.name

    assert f(user) == "LasWonho"


def test_underscore_with_type():
    f = _[str]

    assert f("Las") == "Las"


def test_underscore_with_type_2():
    f = _[User].name

    assert f(User()) == "LasWonho"


def test_underscore_with_type_3():
    f = _[str].lower()

    assert f("ABC") == "abc"
