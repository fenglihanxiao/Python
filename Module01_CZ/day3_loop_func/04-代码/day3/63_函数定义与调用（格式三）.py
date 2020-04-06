"""
演示带返回值的函数定义与调用
定义格式：
def 函数名(参数):
    函数体
    return 具体的返回值
调用格式：
变量名 = 函数名(参数)
"""


def add(a, b):
    # print(a+b)
    return a + b


def div(a, b):
    # print(a/b)
    return a / b


c = add(1000, 2000)
print(c)
d = div(c, 2)
print(d)













