set1 = {1}
print(set1.__sizeof__())

for i in range(2, 100):
    set1.add(i)
    print(i, end="-")
    print(set1.__sizeof__())