"""
演示重写关系中调用父类被覆盖的方法
"""
class Animal:
    def __init__(self):
        print("动物被创建")
    def eat(self):
        print("动物吃东西")

class Cat(Animal):
    def __init__(self):
        print("猫被创建")
        super().__init__()
    def eat(self):
        print("猫吃鱼")
        # 调用格式一：父类名.方法名(对象)
        Animal.eat(self)
        # 调用格式二：super(本类名,对象).方法名（）
        super(Cat,self).eat()
        # 调用格式三：super().方法名（）
        super().eat()

    def __str__(self):
        s = super().__str__()
        print("------------------")
        print(s)
        print("------------------")
        return "喵星人"

cat1 = Cat()
cat1.eat()
print(cat1)
