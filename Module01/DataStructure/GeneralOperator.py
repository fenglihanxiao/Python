list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
dict1 = {1: "aa", 2: "bb", 3: "cc", 4: "dd"}

"""
   1. list and tupel can use "+", need to concatenate with the same type 
   2. Set and dict can't use "+"
"""
print(list1 + list2)
print(tuple1 + tuple2)

print("=====================================")
"""
   1. list and tupel can use "*", need to concatenate with the same type 
   2. Set and dict can't use "*"
"""
print(list1 * 4)
print(tuple1 * 4)

print("=====================================")
"""
   1. List, tuple, set and dict can use in and not in
"""
print(3 in list1)
print(3 not in list1)
print()
print(3 in tuple1)
print(3 not in tuple1)
print()
print(3 in set1)
print(3 not in set1)
print()
print(3 in dict1)
print(3 not in dict1)

print("=====================================")
"""
   1. One iteration of comparision, not related to length
"""
list4 = [2, 1, 2, 1, 2, 3]
list5 = [2, 1, 3]
print(list4 > list5)

print("=====================================")
"""
   1. Set can only use == operator
   2. < and > are not applicable
"""
set4 = {1}
set5 = {2}
print(set4 == set5)