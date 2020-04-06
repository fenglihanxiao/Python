"""
    1. 191_XXX -> Use module partially
"""

###########################################
# 1. Partial import from module
# 2. from ModulePackage.Module_189 import *

# from ModulePackage.Module_189 import show
# from ModulePackage.Module_189 import age
# from ModulePackage.Module_189 import modules
# from ModulePackage.Module_189 import Cat
#
# show()
# print(age)
# print(modules)
# print(Cat.mow())

###########################################
# 1. The last import statement takes effect

from Module01.ModulePackage.Module_189 import age
# from Module01.ModulePackage.Module_191 import age
from Module_189 import age

print(age)
