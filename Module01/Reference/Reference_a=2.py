"""
    1. Reference memory address introduction for int
    2. Reference_a=2.PNG
"""

a = 1
b = 1

# Where is the memory address of 1 reside
print("============================ 1's address")
print(id(1))
print(id(1))


# Address of "a" point to the memory address of 1 reside
print("============================ a=1's address")
print(id(a))
# Address of "b" point to the memory address of 1 reside
print("============================ b's address")
print(id(b))

print("============================ 2's address")
print(id(2))

a = 2

print("============================ a=2's address")
print(id(a))

"""
    1. Reference memory address introduction for bool
    2. Reference_Bool.PNG
"""

print("-------------------------------------")
flag1 = True
flag2 = False

print("============================ True's address")
print(id(True))
print("============================ False's address")
print(id(False))

print("============================ Flag1=True's address")
print(id(flag1))

flag1 = False
print("============================ Flag1=False's address")
print(id(flag1))

print("============================ Flag2=False's address")
print(id(flag2))

"""
    1. Reference memory address introduction for str
    2. Reference_Str.PNG
"""
print("-------------------------------------")
str1 = "a"
str2 = "a"

print(id(str1))
print(id(str2))

str1 = "b"
print("================================ str1=b's address")
print(id(str1))
print(id(str2))
