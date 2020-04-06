class Card:
    def __init__(self):
        self.card_id = None
        # Make private member of pwd
        # __ -> private member
        self.__pwd = "123"

    def set_pwd(self, p):
        self.__pwd = p

    # Make private method
    # __ -> private method
    def __get_pwd(self):
        return self.__pwd


c = Card()
c.set_pwd("456")
#print(c.get_pwd())


class Cat:
    """ Formal way to define member variables"""
    # When you create object, system automatically invoke
    def __init__(self, t, n):
        self.__type = t
        self.__name = n

    def set_type(self, t):
        self.__type = t

    def get_type(self):
        return self.__type

    def set_name(self, n):
        self.__name = n

    def get_name(self):
        return self.__name

c = Cat("Lovely", "Amy")
# c.set_type("Lovely")
# c.set_name("Amy")
print("Cat type=%s;name=%s" % (c.get_type(), c.get_name()))