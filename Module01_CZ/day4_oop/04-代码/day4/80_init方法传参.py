"""
演示__init__传参
"""
class Cat:
    def __init__(self, type, name):
        self.__type = type
        self.__name = name

    def get_type(self):
        return self.__type

    def set_type(self,type):
        self.__type = type

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

cat1 = Cat("英格兰短毛猫","小短毛")
print(cat1.get_type())
print(cat1.get_name())