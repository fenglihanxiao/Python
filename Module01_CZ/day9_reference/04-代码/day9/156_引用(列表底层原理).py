"""
演示引用(列表底层原理)
40          5*8
72      32  5*8 + 4*8
104     32  5*8 + 4*8 +4*8
168     64  5*8 + 4*8 +4*8 8*8
"""
a = []
print(a.__sizeof__())
a.append(1)
print(a.__sizeof__())
a.append(2)
print(a.__sizeof__())
a.append(3)
print(a.__sizeof__())
a.append(4)
print(a.__sizeof__())
a.append(5)
print(a.__sizeof__())
a.append(6)
print(a.__sizeof__())
a.append(7)
print(a.__sizeof__())
a.append(8)
print(a.__sizeof__())
a.append(9)
print(a.__sizeof__())