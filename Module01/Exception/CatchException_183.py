"""
    1. 183_XXX -> Exception handle different causes
"""

try:
    a = "python"
    print(a)
    print(a.index("o"))
    n = 1 / 0

#########################################################
# 1. Catch specific exception
except NameError:
    print("a needs to be defined and use it --------------")

#########################################################
# 1. Catch specific exception
except ValueError:
    print("substring not found --------------")

#########################################################
# 1. Catch unknown (others) exceptions
# 2. The flow has to be specific to abstract Exception
# 3. NameError and ValueError derive from Exception
except Exception:
    print("Unknown exception -----------------")
