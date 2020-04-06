"""
演示重写
"""
class Animal(object):
    def eat(self):
        print("动物吃东西")

class Cat(Animal):
    def eat(self):
        print("猫吃鱼")

    def __str__(self):
        return "喵星人"

cat1 = Cat()
cat1.eat()
print(cat1)
