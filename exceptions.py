# Errors & Exceptions

try:
    # a = 5 / 0
    # b = a + 4
    f = open("some.txt")
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)
finally:
    print("Cleaning up ...")


class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value too high")
    if x < 10:
        raise ValueTooSmallError("Value too small", x)


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


try:
    test_value(5)
except ValueTooSmallError as e:
    print(e.message, e.value)
