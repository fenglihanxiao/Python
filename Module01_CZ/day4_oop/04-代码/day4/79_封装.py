"""
演示私有化属性与封装
"""
class Card:
    def __init__(self):
        self.card_id = None
        self.__pwd = None

    def get_pwd(self):
        return self.__pwd

    def set_pwd(self,pwd):
        self.__pwd = pwd

c = Card()
c.set_pwd("345")
print(c.__get_pwd())

class Cat:
    def __init__(self):
        self.__type = "波斯猫"
        self.__name = None

    def get_type(self):
        return self.__type

    def set_type(self,type):
        self.__type = type

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name