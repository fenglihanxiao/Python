"""
    193_XXX -> Define a module
"""


class Cat():
    def __init__(self):
        self.name = "Lindon"
        self.age = 18

    @classmethod
    def mow(cls):
        print("Cat mow mow ...")


def show():
    print("Hello module ...")
    print("Morning")
    return 10


modules = [1, 2, 3]
age = 18

###################################################
# 1. Filter out when use module which does not execute
#    the test codes here
if __name__ == "__main__":
    print(age)
    print(modules)

print("================")
print("__name__ in module self", __name__)
