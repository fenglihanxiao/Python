#####################################
# 1. Tuple operation
tuple1 = (1, 2, 3, 4, 3, 2, 1)
idx = tuple1.index(4)
idx2 = tuple1.index(3, 3, 6)
print(idx)
print(idx2)

cnt = tuple1.count(1)
print(cnt)

#####################################
# 1. Set operation
set1 = {8, 98, 5, 6}
set1.add(100)
print(set1)