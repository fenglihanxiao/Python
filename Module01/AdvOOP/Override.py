class Animal:

    def eat(self):
        print("Animal eat meat")



class Cat(Animal):
    """ Derived class Cat """
    #######################################
    # Override Animal eat method
    def eat(self):
        print("Cats eat fishes")

    #######################################
    # Override object __str__ method
    def __str__(self):
        return "Cat star!"


an = Animal()
an.eat()

cat = Cat()
#######################################
# Override Animal eat method
cat.eat()
print(cat)