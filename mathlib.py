class NumErr(Exception):
    pass


class Divzero(NumErr):
    pass


class Oflow(NumErr):
    pass


...


def func():
    ...
    raise Divzero()
