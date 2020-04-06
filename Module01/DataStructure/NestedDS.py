list1 = [99, 8, 101]
list2 = [1, 2, 3]
tuple1 = (101, 32, 121)
set1 = {84, 32}
# Concatenate many ds
list4 = [list1, list2, tuple1, set1, 9]

for outer in list4:
    if isinstance(outer, list) or isinstance(outer, tuple) or isinstance(outer, set):
        for inner in outer:
            print(inner)
    else:
        print(outer)
    print("===============================")