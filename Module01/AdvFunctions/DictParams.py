"""
    1. Use for position param, variable params, keyword argument
"""
def test(a, b, *args, m=1, n=2):
    print(a)
    print(b)
    print(args)
    print(m)
    print(n)

test(1, 2, 3, 4, 5)
print()
test(1, 2, 3, 4, 5, m=10, n=20)
print()
"""
    1. Use **kwargs for dict on keyword arguments
"""
def foo(**kwargs):
    print(kwargs)

foo(a=10, b=20)
print()

def test2(a, b, *args, m=1, n=2, **kwargs):
    print(a)
    print(b)
    print(args)
    print(m)
    print(n)
    print(kwargs)

###############################################
# 1. position args, *args, keyword args, dict args
test2(1, 2, 3, 4, 5, m=10, n=20, x=100, y=200)
print()

def test3(m, **kwargs):
    print(m)
    print(kwargs)

test3(2, x=12, y=24)
