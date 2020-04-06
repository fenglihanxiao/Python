"""
演示循环程序的书写误区
案例：计算100以内的偶数的和
"""
# 分析
# 1.100以内的数字是1到100
# 2.求和要有一个变量来保存最终的计算结果 sum
# 2.1只有满足偶数的条件，才加入到sum中
# 3.使用while循环来构造反复加的操作

# num = 1
# sum = 0
# while num <= 100:
#     # 满足是偶数才加入到sum中
#     if num % 2 == 0:
#         sum = sum + num
#     num += 1
# print("100以内的偶数和是：%d" % sum)

# 案例：计算100以内的偶数的和
num = 2
sum = 0
while num <= 100:
    sum += num
    num += 2
print("100以内的偶数和是：%d" % sum)

# 计算所有3位数中35的倍数的数值的和
num = 100
sum = 0
while num <= 999:
    if num % 35 == 0 :
        sum += num
    num += 1
