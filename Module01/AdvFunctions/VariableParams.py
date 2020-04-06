"""
    1. *args
"""
# def sum(a, b, c):
#     sum = a + b + c
#     print(sum)
#
# sum(1, 2, 3)


"""
    1. only define one *args
"""
def _sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

val = _sum(1,2,3,4,5)
print(val)
print()

"""
    1. system define sum
"""
print(sum([0, 1, 2, 3, 4], 2)) # 列表计算总和后再加 2
print()

"""
    1. Position argument has to proceed before *args
"""
def foo(a, b, *args):
    print(a)
    print(b)
    print(args)

# TypeError: foo() missing 1 required keyword-only argument: 'c
# def foo(a, *args, c):

foo("feng", 18, "itcast", 18)
print()

"""
    1. Use keyword argument to specify params
    2. Keyword arguments need to be placed after *args 
"""
def bar(*args, a, b):
    print(args)
    print(a)
    print(b)

# 1. Use keyword argument to specify params
# 2. Keyword arguments need to be placed after *args
bar(1,2,3,4, a=18, b=65)
print()
"""
    1. Use print function to apply for variable params
    2. Keyword arguments need to be placed after *args 
"""
print("a", "b", "c", "d", sep="|")