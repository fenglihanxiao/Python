"""
演示循环嵌套中的break与continue
"""
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print("%d*%d=%d" % (i, j, i * j), end="\t")
        i += 1
    print()
    if j == 6:
        break
    j += 1

