"""
    1. **kwargs usage
"""
def test(**kwargs):
    # Do not use **kwargs

    # Print key serials
    print(*kwargs)

    _dict = kwargs
    for k in _dict.keys():
        print("Key=", k)
        print("Value=", _dict[k])
        print()

test(a=1, b=2, c=3)

"""
    1. * -> unpack container type
"""
list1 = [1, 2, 3]
tuple1 = (3, 4, 5)
set1 = {5, 6, 7}
dict1= {"aa": 123, "bb": 456, "cc": 789}
str1 = "itcast"

print(*list1)

def test2():
    return 3, 4, 5

# uppack container
a, b, c = test2()