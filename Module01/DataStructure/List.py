list1 = [1, 2, 3, "itcast", "test", True, False, None, "test"]
# print(list1)
# print(list1[4])
# list1[4] = "Black horse"

list1.append("xyz")
list2 = list1.copy()
idx = list1.index("test")
idx = list1.pop(3)

for data in list1:
    print(data)

