# val = 365
#
# a = 365 // 100
# b = 365 % 100
# c = b // 10
# d = b % 10
#
# print("%d,%d,%d,%d" % (a, b, c, d))
#
# n = 123
# while n > 0:
#     (n, r) = divmod(n,10)
#     print(r)

val2 = 123
x = val2
y = val2
while y > 0:
    num = y % 10
    #y = int(y / 10)
    y = y // 10
    print("num=%d,y=%d" % (num, y))