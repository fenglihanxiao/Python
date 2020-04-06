"""
演示引用(集合)
"""
# print(id({}))
# print(id({}))
# print(id({1,2,3}))
# print(id({1,2,3}))
# print(id({3,2,1}))
# print(id({1,2,3,4}))

# a = {1,2,3}
# b = {1,2,3}
# print(id(a))
# print(id(b))

a = {1,2,3}
b = a
a.add(4)
print(a)
print(b)
print(id(a))
print(id(b))
