"""
演示引用(数值型、布尔型、字符串型特殊现象)
"""
# print(id(256))
# print(id(256+0))
# print(id(257))
# print(id(257+0))
# print(id(-5))
# print(id(-5+0))
# print("------------")
# print(id(-6))
# print(id(-5-1))
# print(id(-4-2))
# print(id(-3-3))
# print(id(-3-3))

# print(id(True))
# print(id(False))

# 0 表示假 非0 表示真
# flag1 = True and 0
# flag2 = 0 and True
# flag3 = 4 or False
# flag4 = False or -5
# print(flag1)
# print(flag2)
# print(flag3)
# print(flag4)

# print(id(True))
# print(id(False))
# print(id(True and 0))
# print(id(0))
# print(id(False or -5))

# print(id(2.0))
# print(id(2.0))

# print(id("aa"))
# print(id("a"+"a"))

print(id("1a%"+"aa"))
print(id("1a%"+"aa"))
# 字母，数字，下划线范围内，相同，其他不同





