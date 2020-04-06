list1 = [5, 8, 12, 6, 8, 6]
list1.sort(reverse=True)
print(list1)

########################################
# 1. Now tuple1 can not write
tuple1 = tuple(list1)
print(tuple1)

########################################
# 1. Now set1 can not contain duplicate
set1 = set(list1)
print(set1)

########################################
# 1. Can be chain
items = tuple(set(list1))
print(items)

tuple2 = {1, 2, 3, 4, 5}

########################################
# 1. list2 can be changed
list2 = list(tuple2)
print(list2)

set2 = {1, 2, 3, 4, 5}
########################################
# 1. list3 can be used by indexer
# 2. Data only can be unique
list3 = list(set2)

########################################
# 1. tuple3 can be used by indexer
tuple3 = tuple(set2)