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


def test_underscore_with_type_4():
    f = _[str].split(" ")

    assert f("A B C") == ["A", "B", "C"]


def test_underscore_with_type_5():
    f = _[str].lower().split(" ")

    assert f("A B C") == ["a", "b", "c"]


def test_underscore_with_type_6():
    f = _[str].split(" ")[0]

    assert f("A B C") == "A"
