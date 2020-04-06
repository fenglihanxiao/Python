"""
    1. The id are the same because it is not been referenced
"""

# print(id([]))
# print(id([]))
#
# print("=================")
#
# print(id([1, 2, 3]))
# print(id([1, 2, 3]))

"""
    1.  Every time list has allocated space. 
        It allocated separate new memory address for it.
"""
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))
# print(id(b))

"""
    1.  b point to a's address, then a and b share the same memory address
"""
a = [1, 2, 3]
print(id(a))
b = a
a.append(4)
print(id(a))
print(id(b))