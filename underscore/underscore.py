class Underscore:
    def __call__(self, value):
        return value

    def __add__(self, number):
        def wrapper(value):
            return value + number
        return wrapper


_ = Underscore()
