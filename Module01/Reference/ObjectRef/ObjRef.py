

class User:
    def __init__(self, name="UK", age="-1"):
        self.name = name
        self.age = age

"""
    1. Obj has different ref has unique memory address 
"""
# u1 = User()
# u2 = User()
# print(id(u1))
# print(id(u2))

"""
    1. Obj assignment has the same address
"""
u1 = User()
u2 = u1
print(id(u1))
print(id(u2))