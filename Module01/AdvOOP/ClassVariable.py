class Cat:
    ###########################################################
    # Class's data member
    subject = "Cat category"

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
print("Cat subject=%s;type=%s;name=%s" % (c.subject, c.get_type(), c.get_name()))

#############################################################
# Access by class name, this is recommended way
print(Cat.subject)

#############################################################
# Access by instance name, this is not recommended way
print(c.subject)

#############################################################
# Write class variable by only class name
Cat.subject = "Tiger Category"
print(Cat.subject)

#############################################################
# Write instance variable, only generate an additional instance variable
c.subject = "Try to change"
print(Cat.subject)


#############################################################
class Chinese:
    country = "China"

    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name

    @classmethod
    def show_country(cls):
        print("We are Chinese and from %s" % Chinese.country)
        c1 = cls("007", "Jame")
        return c1.id_num, c1.name


chi = Chinese("5109", "Feng")
id, name = Chinese.show_country()
# chi.show_country()
print("========")