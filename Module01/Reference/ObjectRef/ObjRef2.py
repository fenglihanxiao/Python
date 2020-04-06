"""
    1. Obj has different ref has unique memory address
"""


class User:
    def __init__(self):
        self.name = "Feng"
        self.age = 18
        self.gender = 1
        self.nick_name = "live"


user1 = User()

##############################################################
# Add member variables does not change sizeof user1
print(user1.__sizeof__())

print(user1.__dict__)
