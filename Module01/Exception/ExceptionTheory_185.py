"""
    1. 185_XXX -> Exception theory
"""

x = 1
y = 0

######################################################
# 1. raise can construct application exception
if y == 0:
    raise ZeroDivisionError("My error message")

z = x / y