tuple1 = (1, 2, 3, "itcast", "test", True, False, None, "test")
tuple2 = ("amy", "stephanie")
print(tuple1)
t3 = tuple1 + tuple2
print(t3)

#######################################
# One element of tuple declaration has to put "," after element
tuple2 = ("str type",)
print(type(tuple2)) # -><class 'tuple'>

tuple3 = ("str type")
print(type(tuple3)) # -> <class 'str'>

#######################################
# Tuple can not be written
# tuple1[4] = "can not modified"

#######################################
# Same iteration as list
for item in tuple1:
    print(item)

#######################################
# Return a tuple
def foo():
    # It seems return multiple vals, but in fact it return a tuple
    return (3, 5)

#######################################
# Use  a tuple
print("Name=%s;Action=%s" % (tuple1[3], tuple1[4]))

a, b = foo()
