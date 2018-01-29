'''
示例：对方法应用装饰器-用装饰器手动跟踪
'''
def tracer(func):
    calls = 0

    def onCall(*args, **kargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kargs)
    return onCall


import time


def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kargs):
            start = time.clock()
            result = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
                return result
            onCall.alltime = 0
            return onCall
        return onDecorator
