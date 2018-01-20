'''
注意：一旦捕获了错误，控制权会在捕捉的地方继续下去（即try之后），没有直接的方式可以回到异常发生的地方（这里是函数kaboom中）
这会让异常更像是简单的跳跃，而不是函数调用：没有办法回到触发错误的代码
'''
def kaboom(x, y):
    print(x + y)


try:
    kaboom([0, 1, 2], 'spam')
except TypeError:
    print('Hello world!')
print('resuming here')
