import time


def timer(label='', trace=True):  # On decorator args: retain args
    def onDecorator(func):  # On @: retain decorated func
        def onCall(*args, **kargs):  # On calls: call original
            start = time.clock()  # State is scopes + func attr
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

# Test on functions


@timer(trace=True, label='[CCC]==>')
def listcomp(N):  # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]  # listcomp(...) triggers onCall


@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))  # list() for 3.0 views


for func in (listcomp, mapcall):
    result = func(5)  # Time for this call, all calls, return value
    func(5000000)
    print(result)
    print('allTime = %s\n' % func.alltime)  # Total time for all calls

# Test on methods


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @timer()
    def giveRaise(self, percent):  # giveRaise = timer()(giveRaise)
        self.pay *= (1.0 + percent)  # tracer remembers giveRaise

    @timer(label='**')
    def lastName(self):  # lastName = timer(...)(lastName)
        return self.name.split()[-1]  # alltime per class, not instance


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20)  # runs onCall(sue, .10)
print(bob.pay, sue.pay)
print(bob.lastName(), sue.lastName())  # runs onCall(bob), remembers lastName
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))
