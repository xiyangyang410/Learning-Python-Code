class Squares:
    '''
    在这里，迭代器对象就是实例self，因为next方法是这个类的一部分。在较为复杂的场景中，迭代器对象可以定义为个别的类或者有自己的状态信息的对象，对相同数据支持多种迭代
    以Python raise语句发出信号表示迭代结束
    '''

    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


if __name__ == '__main__':
    for i in Squares(1, 5):
        print(i, end=' ')
