"""
演示引用(对象存储原理)
"""
class User:
    def __init__(self):
        self.name = "张三"
        self.age = 18
        self.gender = "男"
        self.id_card = "1007"

user1 = User()
# print(user1.__sizeof__())

print(user1.__dict__)