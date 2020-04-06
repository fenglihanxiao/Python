"""
演示列表、元组、集合的格式转换
"""
list1 = [1,2,3,4,5,4,5]
print(tuple(list1))
print(set(list1))
print(tuple(set(list1)))
tuple1 = (1,2,3,4,5)
print(list(tuple1))
print(set(tuple1))
set1 = {1,2,3,4,5}