"""
演示递归调用
"""
# 求1到指定数字的和（100）
# sum(100) = sum(99)+100
# sum(99) = sum(98)+99
# sum(2) = sum(1)+2
# sum(1) = 1

# def sum(num):
#     #设置结束标志
#     if num == 1:
#         return 1
#     return sum(num-1)+num
#
# print(sum(100)) #5050

def sum(num):
    #设置结束标志
    if num == 1:
        return 1
    return sum(num-1)+num

print(sum(999))


