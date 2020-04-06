"""
演示引用(集合存储原理)
"""
set1 = {1}
print(set1.__sizeof__())
for data in range(2,100):
    set1.add(data)
    print(data,end="-")
    print(set1.__sizeof__())
