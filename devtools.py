'''
针对位置参数的一个基本范围测试装饰器

__debug__内置变量——Python将其设置为True，除非它将以-O优化命令行标志运行
当__debug__为 False 的时候，装饰器返回未修改的最初函数，以避免额外调用及其相关的性能损失
'''


def rangetest(*argchecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator
