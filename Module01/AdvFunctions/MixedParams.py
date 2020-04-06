"""
    1. Keyword param
"""

def foo(a = 100, b = 10):
    print(a)
    print(b)

foo(b=200, a=1000)

foo(1, b=15)

# Problem
# SyntaxError: positional argument
# follows keyword argument
# foo(b=30, 1)
"""
    1. key word argument needs to place after position argument
    2. 根据我查资料总结结果，很多 python 内置的函数都不支持 keyword 参数，python 的内置函数都是 c 实现的，只支持位置参数
"""

print("hello", "abc", sep="|", end=" ")
print("itcast")