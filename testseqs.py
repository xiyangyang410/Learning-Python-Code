from mytools import timer


@timer(label='[CCC]==>')
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))


for func in (listcomp, mapcall):
    print('')
    result = func(5)
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s' % func.alltime)
print('map\comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
