"""
演示文档注释使用
"""


def say_hello():
    """打印hello python"""
    print("hello python")


def sum_1_100():
    """用于计算1到100的和"""
    i = 1
    sum = 0
    while i <= 100:
        sum += i
        i += 1
    print(sum)


say_hello()
sum_1_100()

