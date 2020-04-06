"""
演示作用域
"""
# def max2(num1, num2):
#     # a = 10
#     # print(a)
#     print(c)
#     if num1 > num2:
#         print("%d和%d中的较大的数字是%d" % (num1, num2, num1))
#     else:
#         print("%d和%d中的较大的数字是%d" % (num1, num2, num2))
#
# def min2(num3, num4):
#     # b = 20
#     # print(b)
#     print(d)
#     if num3 < num4:
#         print("%d和%d中的较小的数字是%d" % (num3, num4, num3))
#     else:
#         print("%d和%d中的较小的数字是%d" % (num3, num4, num4))
#
# c = 20
# d = 30
#
# max2(c,d)
# min2(3,4)


"""全局变量与局部变量的冲突"""
def test():
    global x
    x = 10
    print(x)

x = 20
test()
print(x)





