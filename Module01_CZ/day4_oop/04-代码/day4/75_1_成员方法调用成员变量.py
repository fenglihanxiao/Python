"""
演示成员方法调用成员
"""
class Cat:
    def __init__(self):
        self.type = "波斯猫"
        self.name = None

    # def introduce(self):
    #     print("我是一只%s，我叫%s" % (self.type, self.name))

    def introduce(self):
        print("我是一只%s，我叫%s，我穿的衣服是%s" % (self.type, self.name, self.color))

cat1 = Cat()
cat1.name = "大帅"
cat1.color = "红色"
cat1.introduce()

cat2 = Cat()
cat2.name = "小帅"
cat2.introduce()