'''
实例：属性验证：使用__getattr__来验证
通过在该实例上存储 name ，它确保了未来的访问不会触发 __getattr__ 。相反， acct 存储为
_acct ，因此随后对 acct 的访问会调用 __getattr__
'''


class CardHolder:
    acctlen = 8  # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct  # Instance data
        self.name = name  # These trigger __setattr__ too
        self.age = age  # _acct not mangled: name tested
        self.addr = addr  # addr is not managed
        # remain has no data

    def __getattr__(self, name):
        if name == 'acct':  # On undefined attr fetches
            return self._acct[:-3] + '***'  # name, age, addr are defined
        elif name == 'remain':
            return self.retireage - self.age  # Doesn't trigger __getattr__
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name':  # On all attr assignments
            value = value.lower().replace(' ', '_')  # addr stored directly
        elif name == 'age':  # acct mangled to _acct
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value  # Avoid looping


if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep=' / ')
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')
