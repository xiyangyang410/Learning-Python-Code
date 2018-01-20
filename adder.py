class Adder:
    def add(self, y):
        print("Not Implemented")

    def __init__(self, start=[]):
        self.data = start

    def __add__(self, other):
        return self.add(other)

    def __radd__(self, other):
        return self.add(other)


class ListAdder(Adder):
    def add(self, y):
        return self.data + y


class DictAdder(Adder):
    def add(self, y):
        new = {}
        # for k in self.keys():
        #     new[k] = self[k]
        for k in y.keys():
            new[k] = y[k]
        return new


if __name__ == '__main__':
    x = Adder()
    # x.add(1, 2)
    x.add(2)
    x = ListAdder()
    # print(x.add([1], [2]))
    print(x.add([2]))

    x = DictAdder()
    # print(x.add({1: 1}, {2: 2}))
    print(x.add({2: 2}))

    x = Adder([1])
    x + [2]
    x = ListAdder([1])
    print(x + [2])
    [2] + x
