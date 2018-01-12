def countLines(file):
    file.seek(0)
    return len(file.readlines())


def countChars(file):
    file.seek(0)
    return len(file.read())


def test(name):
    file = open(name)
    return countLines(file), countChars(file)


if __name__ == '__main__':
    print(test("mymod2.py"))
