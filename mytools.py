'''
把最初的 Timer 类嵌入一个封闭的函数中，以便创建一个作用域
以保持装饰器参数。外围的 timer 函数在装饰发生前调用，并且它只是返回 Timer 类作为
实际的装饰器。在装饰时，创建了 Timer 的一个实例来记住装饰函数自身，而且访问了
位于封闭的函数作用域中的装饰器参数
'''
import time


def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kargs):
            start = time.clock()
            result = self.func(*args, **kargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result

    return Timer
