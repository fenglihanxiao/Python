"""
    1. 167_XXX
    2. Define operator new
"""


class User:
    def __new__(cls, *args, **kwargs):
        #####################################
        # Add init operation logic here
        # 1. init hardware device
        # 2. Do data init, e.g., remote turn on computer
        # 3. Init camera device
        print("User new method is running .............")

        #####################################
        # Call object base class new and need return instance
        instance = object.__new__(User)
        return instance

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("User init method is running ....")


user1 = User("Feng", 18)
print(user1.name)
print(user1.age)

del user1.name
print(user1.name)
