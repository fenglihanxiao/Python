"""
演示匿名函数使用注意事项
"""
# def add( a,b ):
#     return a + b
# c =  add(3,4)
# print(c)
#
# d = (lambda a,b : a + b)(4,5)
# print(d)

# 1.无参数,可以
# f1 = (lambda : 100)()
# print(f1)

# 2.多返回值,不可以    # TypeError: 'tuple' object is not callable
# f2,f3 = (lambda :(3,4))()
# print(f2)
# print(f3)

# 3.无返回值,不成立    # TypeError: 'tuple' object is not callable
# x = (lambda : (print("hello"),print("itcast")))()
# print(x)

# 4.数据存储模型
f4 = (lambda :[a**2 for a in range(5) if a % 2 == 0])()
print(f4)