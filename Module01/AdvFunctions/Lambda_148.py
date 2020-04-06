"""
    1. 148_XXX -> define lambda three forms
"""

#########################################################
# 1. No params

f1 = (lambda : 100)()
print(f1)

#########################################################
# 1. Return a tuple

f2, f3 = (lambda a, b: (a + 1, b +2))(10,12)
print(f2)
print(f3)
print((lambda a, b: (a + 1, b +2))(10,12))