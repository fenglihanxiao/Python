"""
    1. 190_XXX -> Use module mix
"""

###########################################
# import Module01.ModulePackage.Module_189
#
# print(Module01.ModulePackage.Module_189.age)
# print(Module01.ModulePackage.Module_189.modules)
# print(Module01.ModulePackage.Module_189.show())
# cat = Module01.ModulePackage.Module_189.Cat()
# print(id(cat))

import Module_189





###########################################
# import Module_189
# print(Module_189.age)
# print(Module_189.modules)
# print(Module_189.show())
# cat = Module_189.Cat()
# print(id(cat))

###########################################
# Right click ModulePackage -> Mark Dir as Source Root
# from Module_189 import *
# from Module_189 import modules
# from Module_189 import show
# from Module_189 import Cat

from Module_189 import *
# print(age)
print(Module_189.modules)
print(show())
cat = Cat()
print(id(cat))