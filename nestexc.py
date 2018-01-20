def action2():
    print(1 + [])


def action1():
    try:
        action2()
        print('AAA')
    except TypeError:
        print('inner try')


try:
    action1()
except TypeError:
    print('outer try')

try:
    try:
        action2()
    except TypeError:
        print('inner try')
except TypeError:
    print('outer try')
