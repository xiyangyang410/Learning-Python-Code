import sys
import traceback


def safe(entry, *args):
    try:
        entry(*args)
    except:
        traceback.print_exc()
        print('Got', sys.exc_info()[0], sys.exc_info()[1])


import oops
safe(oops.oops)
