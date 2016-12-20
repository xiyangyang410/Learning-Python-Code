"""
在Python2中模拟Python3的print函数
print30(*args,sep=' ',end='\n',file=None)
"""
import sys


def print30(*args, **kargs):
    sep = kargs.get('sep', ' ')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ' '
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


def print30v2(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs:
        raise TypeError('extra keywords: %s' % kargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
