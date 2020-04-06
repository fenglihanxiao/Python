"""
    1. 165_XXX: pass by ref
"""
def foo(x):
    x.append("feng")

list1 = ["hello", "python"]
print(list1)
print("==================================")
foo(list1)
print(list1)

print("####################################")
"""x
    1. pass by ref version 2
"""
def foo(x):
    x = [1, 2, 3]

list1 = ["hello", "python"]
print(list1)
print("==================================")
foo(list1)
print(list1)
