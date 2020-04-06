"""
演示引用(对象)
"""
class User:
    def __init__(self,name="未知",age="-1"):
        self.name = name
        self.age = age

# print(id(User()))
# print(id(User()))
# print(id(User()))
# print(id(User()))
# user1 = User()
# user2 = User()
# print(id(user1))
# print(id(user2))
# print(id(User()))
# print(id(User()))

user1 = User()
user2 = user1
user3 = User()
user1.name="张三"
print(user1.name)
print(user2.name)
print(user3.name)

