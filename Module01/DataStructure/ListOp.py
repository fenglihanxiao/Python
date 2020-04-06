list1 = [1, 2, 3, "itcast", "test", True, False, None, "test"]
list1.append(10)

print(list1)

print(list1.__len__())

count = list1.count("test")
print(count)

list2 = [5, 8, 4]
list3 = [99, 2]
list2.extend(list3)
print(list2)

tuple1 = (21, 11)
list2.extend(tuple1)
print(list2)

set1 = {100, 76}
list2.extend(set1)
print(list2)

#####################################################################

print("============================================")

array = ["a", "b", "c"]
array.pop()

for item in array:
    print(item)

for index in range(len(array)):
    print(str(index)+".."+array[index])


for index,val in enumerate(array):
    print(str(index)+"--"+val);


# #166 excersize
g_list = [1, 2, 3]

def list_test(lst):
    lst = lst + lst
    # Test for this too
    lst += lst

list_test(g_list)
print(g_list)