class Mylist():
    def __init__(self, start):
        '''
        通过该附加而不是分片复制初值，否则结果就不是真正的列表，也就痐相应预期的列表方法
        例如，对字符串进行分片运算会传回另一字符串，而不是列表
        '''
        # self.wrapped = start[:]
        self.wrapped = []
        for x in start:
            self.wrapped.append(x)

    def __add__(self, other):
        return Mylist(self.wrapped + other)

    def __mul__(self, time):
        return Mylist(self.wrapped * time)

    def __getitem__(self, offset):
        return self.wrapped[offset]

    def __len__(self):
        return len(self.wrapped)

    def __getslice__(self, low, high):
        return Mylist(self.wrapped[low:high])

    def append(self, node):
        self.wrapped.append(node)

    def __getattr__(self, name):
        return getattr(self.wrapped, name)

    def __repr__(self):
        return repr(self.wrapped)


if __name__ == '__main__':
    x = Mylist('spam')
    print(x)
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x * 3)
    x.append('a')
    x.sort()
    for c in x:
        print(c, end=' ')
