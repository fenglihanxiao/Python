"""
演示字典参数格式混用
"""
# def test(a,*args,m=1, **kwargs):
#     print(kwargs)

def test(a,*args,m=1, **kwargs):
    print(a)
    print(args)
    print("m=", m)
    print(kwargs)

test(10, 1, 2, 2, m = 4, x = 1, y = 2)
print("="*20)
test(10, 1, 2, x = 1, y = 2)

print("*"*20)


# def test(m,**kwargs):
#     print(m)
#     print(kwargs)
#
# test(x=1,y=2,m=1)
