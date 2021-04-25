class Underscore:
    def __call__(self, value):
        return value

    def __add__(self, number):
        def wrapper(value):
            return value + number

        return wrapper

    def __getattr__(self, item: str):
        def wrapper(value):
            return eval(f"value.{item}")

        return wrapper


_ = Underscore()
