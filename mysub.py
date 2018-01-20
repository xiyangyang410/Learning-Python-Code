from mylist import Mylist


class MylistSub(Mylist):
    calls = 0

    def __init__(self, start):
        self.adds = 0
        Mylist.__init__(self, start)

    def __add__(self, other):
        MylistSub.calls += 1
        self.adds += 1
        return Mylist.__add__(self, other)

    def stats(self):
        return self.calls, self.adds


if __name__ == '__main__':
    x = MylistSub('spam')
    y = MylistSub('foo')
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x + ['toast'])
    print(y + ['bat'])
    print(x.stats())
