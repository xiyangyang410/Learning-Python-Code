'''
ListInstance使用以下技巧类提取实例的类名和属性：
    1. 每个实例都有一个内置的__class__属性，他引用自己所创建自的类，并且每个类都有一个__name__属性，他引用了头部中的名称
    因此，表达式self.__class__.__name__获取了一个实例的类的名称

    2. 这个类通过直接扫描实例的属性字典（他从__dict__中导出），以构建一个字符串来显示所有实例属性的名称和值
    字典的键通过排序，以避免Python跨版本的任何排序差异

类显示了两种其他技术：
    1. 他通过调用id内置函数显示了实例的内存地址，该函数返回任何对象的地址
        根据定义，这是一个唯一的对象标识符
    
    2. 他针对其工作方法使用伪私有命名模式：__attrnames，他变成了_ListInstance__attrnames
'''


class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instances via inheritance of __str__, coded here; displays
    instance attrs only; self is the instance of lowest class;
    uses __X names to avoid clashing with Client's attrs
    """

    def __str__(self):
        return '<Instance of %s, addredd %s:\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result
