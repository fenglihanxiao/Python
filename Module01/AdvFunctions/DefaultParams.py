"""
    1. Pass default parameters
"""
# c can not specify after default param b
# def foo(a, b = 10, c):

def foo(a, b = 10):
    print(a)
    print(b)

foo("bar")

str1 = "hello python"
# Use default params
print(str1.index("o"))

# User specify params
print(str1.index("o", 6, 12))


list1 = [1, 2, 3]
# Use default params
print(list1.pop())
print(list1)

# User specify params
print(list1.pop())
print("列表现在为 : ", list1)
print(list1)