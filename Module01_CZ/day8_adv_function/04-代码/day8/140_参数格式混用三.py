"""
演示可变参数格式混用
"""
# def test(*args):
#     for data in args:
#         print(data)
#
# test("张三",18,"itcast",True)

# def test(a,b,c,d ,*args):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
#
# test("张三",18,"itcast",True)


def test(*args,c,d):
    print(args)
    print(c)
    print(d)

test(1,2,3)