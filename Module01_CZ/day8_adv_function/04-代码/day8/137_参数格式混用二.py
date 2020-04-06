"""
演示关键字参数格式混用
"""
# def test(a =100,b=200):
#     print(a)
#     print(b)
# test(b=2,a=1)

# TypeError: test() got multiple values for argument 'a'
# def test( a,b):
#     print(a)
#     print(b)
# test(1,a = 1)

def test01(a, *args):
    print(args)
    print(a)

test01(1, 2, 3)

print("-" * 40)

def test02(*args, a):
    print(args)
    print(a)

test02(1, 2, 3, a = 4)

print("a", "b", "c", sep=";", end="|||")