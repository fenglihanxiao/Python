"""
 1. Define min and max function to compute variable params
"""


def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def my_min(a, b):
    if a < b:
        return a
    else:
        return b


def it_min_max(*args):
    _max = args[0]
    _min = args[0]
    j = 0

    for i in args:
        _max = my_max(i, _max)
        _min = my_min(i, _min)
        j = i
    return _min, _max


def min_max(*args):
    _max = max(args)
    _min = min(args)
    return _min, _max

# r1 = min_max(99, 2, 18, 67, 174)
# print(r1)

r2 = it_min_max(99, 2, 18, 175, 67)
print(r2)