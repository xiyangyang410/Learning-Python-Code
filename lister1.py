'''
既然我们也显示继承的方法，我们必须使用__str__而不是__repr__来重载打印
使用__repr__这段代码将会循环，显示一个方法的值，该值触发了该方法的类的__repr__，从而显示该类
即，lister的__repr__试图显示一个方法，显示该方法的类将再次触发lister的__repr__
'''


class ListInstance:
    """
    Use dir() to collect both instance attrs and names
    inheritanced from its classes; Python3.0 shows more
    name than 2.6 because of the implied object superclass
    in the new-style class module; getattr() fetches inheritanced
    names not in self.__dict__; use __str__, not __repr__,
    or else this loops when printing bound methods
    """

    def __str__(self):
        return '<Instance of %s, addredd %s:\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            # if attr[:2] == '__' and attr[-2:] == '__':
            #     result += '\tname %s=<>\n' % attr
            # else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result
