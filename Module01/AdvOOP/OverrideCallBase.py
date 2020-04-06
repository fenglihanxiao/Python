class Animal:

    def __init__(self):
        print("================= Animal ctor")

    def eat(self):
        print("Animal eat meat")



class Cat(Animal):
    def __init__(self):
        #######################################
        # Third __init__ method to call base eat.
        # It is a preferred way to use
        #######################################
        super().__init__()
        print("================= Cat ctor")

    """ Derived class Cat """
    #######################################
    # Override Animal eat method
    def eat(self):
        print("Cats eat fishes")

        #######################################
        # First method to call base eat
        Animal.eat(self)

        #######################################
        # Second method to call base eat
        super(Cat, self).eat()

        #######################################
        # Third method to call base eat.
        # It is a preferred way to use
        #######################################
        super().eat()

    def __str__(self):
        s = super().__str__()
        print("==================================")
        print(s)
        print("==================================")
        return "Mars cat"

cat = Cat()
#######################################
# Override Animal eat method
cat.eat()

print(cat)