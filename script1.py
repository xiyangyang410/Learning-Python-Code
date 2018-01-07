import sys
'''
在Windows中，还有一种完全阻止弹出DOS终端窗口的方法。以pyw为扩展名的文件只显示由脚本构建的窗口，而不是默认的DOS终端窗口。
pyw文件是拥有这种特别窗口操作行为的.py文件。他们常常应用于Python编码的用户界面（这些用户界面构建自己的窗口），和各种其他技术一起使用，把打印完成的输出和错误保存到文件中。
'''
print(sys.platform)
print(2 ** 100)
x = 'Spam!'
print(x * 8)
input()
