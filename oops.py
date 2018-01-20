class MyError(Exception):
    pass


def oops():
    raise MyError('spam!')


def doomed():
    try:
        oops()
    except IndexError:
        print('caught an index error!')
    except MyError as data:
        print('caught error:', MyError, data)
    else:
        print('no error caught...')


if __name__ == '__main__':
    doomed()
