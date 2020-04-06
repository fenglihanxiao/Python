from Module01.ModulePackage.Module_192 import *

###############################################
# 1. in __all__ list
# 2. This can be only applied in "import *" case
print(age)
show()
cat = Cat()
cat.mow()

###############################################
# 1. Can be specify by modules name
# 2. __all__ does not affect this type of importing
from Module_192 import modules
print(modules)

# Call with module name
import Module_192
print(Module_192.modules)



