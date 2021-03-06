"""
演示三个数字求最大值函数案例
要求1：任意给出两个数字，可以得到最大的数字值
要求2：基于最大值函数基础上制作
"""
# 分析
# 1.两个函数，一个是求两个数字的最大值，还有一个是求三个数字的最大值
# 2.三个数字的最大值函数调用两个数字最大值函数来完成任务
# 3.最终结果要使用return 返回

# 两个数字求最大值
def max2(a, b):
    if a > b:
        return a
    else:
        return b

def max3(a, b, c):
    # 先使用两个数字求出最大值
    x = max2(a,b)
    # 使用得到的结果再与第三个数字一起求最大值
    y = max2(x,c)
    return y

m = max3(1,3,5)
print(m)



