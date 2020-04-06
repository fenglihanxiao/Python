"""
演示del方法
"""
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print("user object is del")

# u1 = User("张三",18)
# del u1
# print(u1)
# print("结束")

u1 = User("aa",11)
u2 = u1
del u1
print("结束")
