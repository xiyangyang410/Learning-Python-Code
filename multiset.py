from setwrapper import Set


class MultiSet(Set):
    '''
    Inherits all Set names, but extends intersect
    and union to support multiple operands; note
    that "self" is still the first argument (stored
    in the *args argument now); also note that the
    inherited & and | operator call the new methods
    here with 2 arguments, but processing more than
    2 requires a method call, not an expression:
    '''

    def intersect(self, *others):
        res = []
        for x in self:
            for other in others:
                if x not in other:
                    break
            else:
                res.append(x)
        return Set(res)

    def union(*args):
        res = []
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return Set(res)


if __name__ == '__main__':
    x = MultiSet([1, 2, 3, 4])
    y = MultiSet([3, 4, 5])
    z = MultiSet([0, 1, 2])

    print(x & y, x | y)  # Two operands

    print(x.intersect(y, z))  # Three operands

    print(x.union(y, z))
    print(x.intersect([1, 2, 3], [2, 3, 4], [1, 2, 3]))  # Four operands
    print(x.union(range(10)))  # Non-MultiSets work, too
