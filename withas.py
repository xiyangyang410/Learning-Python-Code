'''
这个类的__exit__方法返回False来传播该异常
__enter__方法返回self，作为赋值给as变量的对象。在其他情况下，这里可能会返回完全不同的对象
运行时，环境管理器会以__enter__和__exit__跟踪with语句代码块的进入和离开
'''


class TraceBlock:
    def message(self, arg):
        print('running', arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception!', exc_type)
            return False


with TraceBlock() as action:
    action.message('test 1')
    print('reached')

with TraceBlock() as action:
    action.message('test 2')
    raise TypeError
    print('not reached')
