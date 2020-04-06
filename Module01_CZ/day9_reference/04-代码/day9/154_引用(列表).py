"""
演示引用(列表)
"""
# print(id([]))
# print(id([]))
# print(id([]))
# print(id([1,2,3]))
# print(id([1,2,3]))
# print(id([1,2,3]))

# a = [1,2,3]
# b = [1,2,3]
# print(id(a))
# print(id(b))


# a = [1,2,3]
# b = [1,2,3]
# a.append(4)
# print(a)
# print(b)
# print(id(a))
# print(id(b))

a = [1,2,3]
b = a
a.append(4)
c = [1,2,3]
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))