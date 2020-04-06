"""
演示del操作
"""
# a = 1
# b = "itcast"
# c = True
# print(a)
# print(b)
# print(c)
# print("------------")
# del c
# print(a)
# print(b)
# print(c)






# list1 = [1,2,3]
# tuple1 = (1,2,3)
# dict1 = {"a":1,"b":2}
# print(list1)
# del list1[0]
# print(list1[0])
# del tuple1[0]
# print(dict1)
# del dict1["a"]
# print(dict1["a"])




class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

u1 = User("张三",18)
u2 = User("张三丰",88)
print(u1.name)
print(u1.age)
del u1.name
print(u2.name)






