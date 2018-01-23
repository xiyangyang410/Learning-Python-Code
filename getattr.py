'''
在Python 3.0下运行的时候， __getattr__ 的结果不同:当通过内置操作获取属
性的时候，没有隐式运行的操作符重载方法会触发哪个属性拦截方法。在解析这样的名
称的时候，Python 3.0省略了常规实例查找机制

· 在Python 3.0中， __str__ 访问有两次未能被 __getattr__ 捕获：一次是针对内置打
  印，一次是针对显式获取，因为从该类继承了一个默认方法（实际上，该类来自内
  置 object ，它是每个类的一个超类）

· __str__ 只有一次未能被 __getattribute__ 捕获，在内置打印操作中，显式获取绕
  过了继承的版本

· __call__在Python 3.0中用于内置调用表达式的两次都没有捕获，但是，当显式获
  取的时候，它两次都拦截到了；和__str__不同，没有继承的__call__默认版本能
  够超越 __getattr__

· __l e n__ 被两个类都捕获了，直接原因是，它在类自身中是一个显式定义的方
  法——它的名称指明了，在Python 3.0中，如果我们删除了类的 __len__ 方法，它不
  会指向 __getattr__ 或 __getattribute__

· 所有其他的内置操作在Python 3.0中都没有被两种方案拦截
'''


class GetAttr:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattr__(self, attr):
        print('getattr:' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattribute__(self, attr):
        print('getattribute:' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None


for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))
    X = Class()
    X.eggs
    X.spam
    X.other
    len(X)

    try:
        X[0]
    except:
        print('fail []')

    try:
        X + 99
    except:
        print('fail +')

    try:
        X()
    except:
        print('fail ()')
    X.__call__()

    print(X.__str__())
    print(X)
