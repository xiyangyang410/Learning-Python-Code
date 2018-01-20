'''
MyList子类扩展了内置list类型的__getitem__索引运算方法，把索引1到N映射为实际的0到N-1
'''
# subclass built-in list type/class
# Map 1..N to 0..N-1; call back to built-in version


class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)


if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')
    print(x)

    print(x[1])
    print(x[3])

    x.append('spam')
    print(x)
    x.reverse()
    print(x)
