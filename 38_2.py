traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)), +']')


def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance:
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)

                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)

                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ', attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator


def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))


def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

# Test code: split me off to another file to reuse decorator


@Private('age')             # Person = Private('age')(Person)
class Person:               # Person = onInstance with state
    def __init__(self, name, age):
        self.name = name
        self.age = age      # Inside accesses run normally


X = Person('Bob', 40)
print(X.name)               # Outside accesses validated
X.name = 'Sue'
print(X.name)
# print(X.age)              # FAILS unles "python －O"
# X.age = 999               # ditto
# print(X.age)              # ditto


@Public('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


X = Person('bob', 40)       # X is an onInstance
print(X.name)               # onInstance embeds Person
X.name = 'Sue'
print(X.name)
# print(X.age)              # FAILS unless "python －O main.py"
# X.age = 999               # ditto
# print(X.age)              # ditto
