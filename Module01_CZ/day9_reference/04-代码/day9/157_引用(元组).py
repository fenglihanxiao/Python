"""
演示引用(元组)
"""
# print(id(()))
# print(id(()))
# print(id((1,2,3)))
# print(id((1,2,3)))

# a = (1,2,3)
# b = (1,2,3)
# print(id(a))
# print(id(b))

a = (4,5,6)
b = a
print(id(a))
print(id(b))