"""
    1. 182_XXX -> Exception handling and else
"""
print("Start program ...")
try:
    a = 1
    print(a)

except:
    print("handler in except")
else:
    #####################################################################
    # 1. If no exception occurs, goes to else: branch, otherwise goes to
    # except branch.
    # 2. Dedicate else block for those code which does not cause exception.
    print("a is printed successfully")


print("End program ...")
