"""
演示str方法的作用
"""
class Cat:
    def __init__(self):
        self.type = "波斯猫"
        self.name = None

    def eat(self):
        print("猫吃鱼")

    def climb(self,meter):
        print("猫会爬树,爬了%d米" % meter)

    def __str__(self):
        return "打印了一只猫"

cat1 = Cat()
print(cat1)

