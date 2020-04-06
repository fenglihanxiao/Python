"""
演示模块局部导入
"""
# from module_189 import show
# from module_189 import age,module
# from module_189 import *
# show()
# print(age)
# print(module)
# Cat.speak()



#模块资源冲突
from module_191 import age
from module_189 import age
print(age)