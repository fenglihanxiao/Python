"""
演示类的成员变量
"""
class Cat:
    def __init__(self):
        self.type = "波斯猫"
        self.name = None


cat1 = Cat()
print(cat1.type)
cat1.name = "大帅"
print(cat1.name)
# 给cat1穿衣服
cat1.cloth = "红色"
cat1.cloth = "蓝色"
print(cat1.cloth)
print("-------------")
cat2 = Cat()
print(cat2.type)
print(cat2.cloth)
print("-------------")
cat3 = Cat()
print(cat3.type)
cat3.name = "小帅"
print(cat3.name)
print(cat3.cloth)