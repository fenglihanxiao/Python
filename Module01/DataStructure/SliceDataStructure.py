"""
    1. Slice only operate on list and tuple, not including set and dict
"""

list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3]
tuple1 = (101, 32, 121)
set1 = {84, 32, 84, 32, 12}
dict1 = {"name": "Feng", "age": 18}

"""
    1. @parm1:      start index
    2. @param2:     end index (exclusive)
    3. @param3:     step
"""
print(list1[1:4:1])

print(list1[1:4:2])

print("=================================")
"""
    1. print(list1[0:4:1]) equals to print(list1[:4:1])

"""
print(list1[0:4:1])
print(list1[0:4:1])

print("=================================")
"""
    1. print(list1[0:6:2]) equals to print(list1[::2])
    2. It can understand that print(list1[0:len(list1):2])

"""
print(list1[0:6:2])
print(list1[::2])

print("=================================")
"""
    1. print(list1[::]) not sliced at all
"""
print(list1[::])

print("Reverse =================================")
print(list1[::-1])

print("=================================")
"""
    1. Slice backwards, last index is not exclusive
"""
print("*" * 40)
print(list1[5:0:-1])
print("*" * 40)
print(list1[-2:-len(list1) - 1:-1])
print("-" * 20)
print(list1[-3:len(list1)])
print("=" * 20)
print(list1[-3:])


txt = "Google#Runoob#Taobao#Facebook"

# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)

print(x)