class Animal:
    type = "Animal"

    """ Base class Animal """
    def __init__(self):
        self.name = None
        self.age = None

    def show(self):
        print("I am an animal %s" % self.name)

    def foo1(self):
        pass


class Cat(Animal):
    """ Derived class Cat """

    def climb(self):
        print("Cat can climb a tree")

    def foo2(self):
        pass


class PersianCat(Cat):

    def foo3(self):
        pass

cat = Cat()
cat.name = "Lindon"
cat.show()

##########################################################
# Call class variable
print(Animal.type)

##########################################################
# __mro__ -> inheritance chain
#   1. (<class '__main__.PersianCat'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)
print(PersianCat.__mro__)

per_cat = PersianCat()
per_cat.foo1()
per_cat.foo2()
per_cat.foo3()

# Test for git diff
per_cat2 = PersianCat()
per_cat2.foo1()
per_cat2.foo2()
per_cat2.foo3()

# Test for git diff 02
per_cat3 = PersianCat()
per_cat3.foo1()
per_cat3.foo2()
per_cat3.foo3()

per_cat3.__class__.type = "Richard"
print(PersianCat.type)


