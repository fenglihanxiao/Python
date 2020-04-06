"""
    192_XXX -> Define a module
"""

############################################
# 1. __all__ expose the module name
__all__ = ["show", "age", "Cat"]

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
