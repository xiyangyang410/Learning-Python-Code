'''
这个例子工作起来就像是对内置字符串进行嵌套循环一样，因为每个循环都会获得独立的迭代器对象类记录自己的状态信息，所以每个激活都有自己在字符串中的位置
'''

class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipObject:
    def __init__(self,wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I),next(I),next(I))

    for x in skipper:
        for y in skipper:
            print(x + y,end = ' ')
    else:
        print('\n')


    