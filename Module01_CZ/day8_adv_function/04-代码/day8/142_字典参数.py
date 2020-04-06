"""
演示字典参数
"""
# def test(a,b,*args,m=1,n=2):
#     print(a)
#     print(b)
#     print(args)
#     print(m)
#     print(n)
#
# test(1,2,3,4,5,m=10,n=20,x=100,y=200,z=300)

def test(**kwargs):
    print(kwargs)   #{'a': 1, 'b': 2}
    for key in kwargs.keys():
        print(key)
        print(kwargs[key])

test(a = 1,b = 2)