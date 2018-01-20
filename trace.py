'''__getattr__会获得属性名称字符串。这个代码利用getattr内置函数，以变量名字符串从包裹对象取出属性：
getattr(X,N)就行是X.N，只不过N是表达式，可在运行时计算出字符串，而不是变量。
事实上，getattr(X,N)类似于X.__dict__[N]，但前者也会执行继承搜索，就行X.N，而getattr(X,N)则不会
'''


class wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)


if __name__ == '__main__':
    x = wrapper([1, 2, 3])
    x.append(4)
    print(x.wrapped)

    x = wrapper({'a': 1, 'b': 2})
    print(x.keys())
