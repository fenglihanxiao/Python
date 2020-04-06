"""
演示可变参数
"""
# def sum(a,b,c):
#     sums = a + b + c
#     print(sums)
#
# sum(1,2,3)

def sum(*args):
    sums = 0
    for num in args:
        sums += num
    print(sums)

sum(1,2,3,4,5)