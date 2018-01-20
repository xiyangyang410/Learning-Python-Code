'''
特定的__contains__拦截成员关系，通用的__iter__捕获其他的迭代环境以至__next__重复被调用，而__getitem__不会被调用
若注释掉__contains__方法后代码的输出发生了变化——成员关系现在路由到了通用的__iter__
若将__contains__和__iter__都注释掉的话，索引__getitem__替代方法会被调用，针对成员关系和其他迭代环境使用连续较高的索引
'''


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end=' ')
        return self.data[i]

    def __iter__(self):
        print('iter=>', end=' ')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end=' ')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print('contaons:', end=' ')
        return x in self.data


X = Iters([1, 2, 3, 4, 5])
print(3 in X)
for i in X:
    print(i, end=' | ')

print()
print([i ** 2 for i in X])
print(list(map(bin, X)))

I = iter(X)
while True:
    try:
        print(next(I), end=' @ ')
    except StopIteration:
        break
