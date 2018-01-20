import sys


def bye():
    sys.exit(40)


try:
    bye()
except:
    print('got it')
print('continuing...')
