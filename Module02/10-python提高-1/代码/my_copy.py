import copy

a = [11, 22]
b = [33, 44]
# Please compare diff with
# c = a + b
c = [a, b]

d = copy.copy(c)
e = copy.deepcopy(c)

a.append(88)
c.append(99)

print("c list=", c)
print("Shadow copy d list=", d)
print("Deep copy d list=", e)