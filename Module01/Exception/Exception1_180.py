"""
    1. 180_XXX -> Exception handling
"""
print("Start program ...")
try:
    # a = 1
    print(a)
    #####################################################################
    # 1. if exception occurred, it will not execute the following statements
    print("a is printed successfully")

except:
    print("handler in except")

print("End program ...")
