"""
演示推导式
表达式 for循环 if 条件
"""
list1 = [i for i in range(1,101)]
print(list1)
list2 = [i for i in range(1,101) if i % 2 == 0 and i % 7 == 0]
print(list2)
list3 = [i**2 for i in range(1,101) if i % 2 == 0 and i % 7 == 0]
print(list3)
list4 = ["good" for i in range(1,101) if i % 2 == 0 and i % 7 == 0]
print(list4)

dict1 = {i:i**2 for i in range(1,8)}
print(dict1)

dict2 = {"aa":"aa1","bb":"bb1"}

dict3 = {dict2[key]:key for key in dict2.keys()}
print(dict3)
