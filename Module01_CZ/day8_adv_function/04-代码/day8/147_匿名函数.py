"""
演示匿名函数
"""
# def add( a,b ):
#     print(a)
#     print(b)
#     print(a + b)
#
# add(3,4)

# def add ( a,b ):
#     return a + b

# add = lambda a,b : a + b
#
# c = add(3,4)
# print(c)

c = (lambda a,b : a + b) (5,4)
print(c)
