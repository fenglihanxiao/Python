"""
演示继承
"""
class Animal:
    type = "动物"
    """父类：动物类"""
    def __init__(self):
        self.name = None
        self.__age = None

    def show(self):
        print("我是一只小动物,我叫%s" % self.name)

class Cat(Animal):
    """子类：猫类"""
    def climb(self):
        print("猫爬树")

c = Cat()
c.name = "大帅"
print(c.name)

c.show()
c.climb()


