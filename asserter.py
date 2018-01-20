'''
assert语句通常是用于验证开发期间程序状况的
显示时，其出错消息正文会自动包括源代码的行信息，以及列在assert语句中的值
'''


def f(x):
    assert x < 0, 'x must be negative'
    return x**2
