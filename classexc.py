'''
sys.exc.info结果的第一个元素就是引发异常的类，第二个是实际引发的实例
这里的用法相当于获取实例的__class__属性
'''


class General(Exception):
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raise0():
    X = General()
    # raise X
    raise General


def raise1():
    X = Specific1()
    # raise X
    raise Specific1


def raise2():
    X = Specific2()
    # raise X
    raise Specific2


for func in (raise0, raise1, raise2):
    try:
        func()
    except General as X:
        import sys
        print('caught:', sys.exc_info()[0], X.__class__)
