"""
    1. 169_XXX
    2. Define operator del
"""


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("User init method is running ....")

    def __del__(self):
        print("User is deleted =================")


#######################################
# 1. del->last stmt

# user1 = User("Feng", 18)
#######################
# 1. Cut down the connection(reference address) and remove object reference
# 2. It does not mean deallocate object memory
# del user1
# print("Last statement ................")

#######################################
# 1. last stmt->del

# user1 = User("Feng", 18)
# print("Last statement ................")

#######################################
# 1. Multiple reference
# 2. It still have reference to User
user1 = User("Feng", 18)
user2 = user1
del user1
#del user2
print("Last statement ................")
