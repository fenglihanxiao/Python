"""
演示返回值
"""


# def max2(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
#
# c = max2(5, 4)
# print(c)

# def test():
#     return 1
#     print("-------")
#     return 2
#
# x = test()
# print(x)

def mul():
    return 3, 4, 5

x,y,z = mul()
print(x)
print(y)
print(z)