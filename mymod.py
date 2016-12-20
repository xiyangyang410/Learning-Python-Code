def countLines(name):
    tot = 0
    for line in open(name):
        tot += 1
    return tot


def countChars(name):
    tot = 0
    for line in open(name):
        tot += len(line)
    return tot


def test(name):
    return countLines(name), countChars(name)

if __name__ == '__main__':
    print(test('mymod.py'))
