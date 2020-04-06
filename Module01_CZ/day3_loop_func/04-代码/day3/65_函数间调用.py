"""
演示函数间调用
"""

def add(a, b):
    return a + b

def div(a, b):
    return a / b

def get(a, b):
    # 先计算和
    c = add(a,b)
    # 再计算平均值
    d = div(c,2)
    return d

x = get(1000,2000)
print(x)


