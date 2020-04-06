"""
演示元组数据修改
"""
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "姓名：%s，年龄：%d" % (self.name,self.age)

tuple1 = (18,"itcast",User("大帅",20),User("小帅",18))
for data in tuple1:
    print(data)
# tuple1[2] = User("张大帅",22)
tuple1[2].age = 22
for data in tuple1:
    print(data)