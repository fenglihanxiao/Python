
class Cat:
    """ Formal way to define member variables"""
    # When you create object, system automatically invoke
    def __init__(self):
        self.__type = "My Dear"
        self.name = "Lindon"
        self.option = None

    def eat(self):
        print("Cat eat fish")

    def climb(self, meter):
        print("Cat climb tree %d feet" % meter)

    def introduce(self):
        """ invoke data member by calling self.data_member"""
        print("I am type=%s, name is %s" % (self.type, self.name))

    def catch(self):
        self.jump()
        self.grasp()
        self.bite()

    def jump(self):
        print("Jump")

    def grasp(self):
         print("grasp")

    def bite(self):
        print("bite")

    # When you print object, system automatically invoke
    def __str__(self):
        return "Address"

cat1 = Cat()
cat1.name = "Amy"
cat1.introduce()
cat1.catch()
my_type = cat1.type
print("my type %s" %(my_type))
