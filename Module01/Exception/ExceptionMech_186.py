"""
    186_XXX -> Mechanism
"""
############################################
# 1. Analyse code from the ROOT to BOTTOM
# 2  Analyse code from the BOTTOM to ROOT
def oper1():
    print(1 / 0)

def oper2():
    oper1()

def oper3():
    oper2()

try:
    oper3()
except:
    print("process Exception here ...")

