"""
演示类的成员方法
"""
class Cat:
    def __init__(self):
        self.type = "波斯猫"
        self.name = None

    def eat(self):
        print("猫吃鱼")

    def climb(self,meter):
        print("猫会爬树,爬了%d米" % meter)

cat1 = Cat()
cat1.eat()
cat1.climb(15)