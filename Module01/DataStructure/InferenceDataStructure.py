"""
    1. List operation
"""
list1 = [i for i in range(1, 101)]
print(list1)

list1 = [i for i in range(1, 101) if i % 2 == 0]
print(list1)

list1 = [i for i in range(1, 101) if i % 2 == 0 and i % 7 ==0]
print(list1)

list1 = [i**2 for i in range(1, 101) if i % 2 == 0 and i % 7 ==0]
print(list1)

list1 = ["cool" for i in range(1, 101) if i % 2 == 0 and i % 7 ==0]
print(list1)

print("==========================================")
"""
    1. Dict operation
"""
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)

"""
    1. Swap dict key value pair
"""
dict2 = {"aa": "aa1", "bb": "bb1", "cc": "cc1"}
print(dict2)
dict3 = {dict2[k]: k for k in dict2.keys()}
print(dict3)


def cond_add():
    lst1 = []
    for i in range(20):
        if i % 2 == 0:
            lst1.append(i)
    return lst1

list1 = cond_add()
print(list1)