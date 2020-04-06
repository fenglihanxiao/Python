"""
    1. Reference memory address introduction
    2. Reference_a=1.PNG
"""

a = 1
b = 1

# Where is the memory address of 1 reside
print("============================ 1's address")
print(id(1))
print(id(1))


# Address of "a" point to the memory address of 1 reside
print("============================ a's address")
print(id(a))
# Address of "b" point to the memory address of 1 reside
print("============================ b's address")
print(id(b))
