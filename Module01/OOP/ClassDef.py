
class Cat:
    """ Formal way to define member variables"""
    # When you create object, system automatically invoke
    def __init__(self):
        self.type = "My Dear"
        self.name = "Lindon"
        self.option = None

    def eat(self):
        print("Cat eat fish")

    def climb(self, meter):
        print("Cat climb tree %d feet" % meter)

    # When you print object, system automatically invoke
    def __str__(self):
        return "Address"

cat1 = Cat()
print("type=%s;name=%s;option=%s" % (cat1.type, cat1.name, cat1.option))
cat1.eat()
cat1.climb(32)
print(cat1)


# cat2 = Cat();
# cat2.type = "Stephanie"
# # Add additional data member to cat2->second way to define data member
# # Not by using class definition, just use object variable
# cat2.cloth = "Purple"
# print("type=%s;name=%s;option=%s;cloth=%s" % (cat2.type, cat2.name, cat2.option, cat2.cloth))
