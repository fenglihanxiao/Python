"""
演示继承关系图
"""
class Animal(object):
    def show1(self):
        pass

class Cat(Animal):
    def show2(self):
        pass

class PersianCat(Cat):
    def show3(self):
        pass

# (<class '__main__.Animal'>, <class 'object'>)
print(Animal.__mro__)
# (<class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)
print(Cat.__mro__)
# (<class '__main__.PersianCat'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)
print(PersianCat.__mro__)

ps = PersianCat()






