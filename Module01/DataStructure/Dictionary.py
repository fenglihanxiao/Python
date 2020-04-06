dict1 = {"aa": "aa1", "bb": "bb1", "cc": "cc1"}
print(dict1)
print(dict1["bb"])
dict1["bb"] = "itcast"
print(dict1)

print("=====================================")

########################################
#   1. Iteration for dict is to get key
#   2. Uses dict1[key] to get value
for key in dict1:
    print(key)
    print(dict1[key])
    print("============")


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name=%s;Age=%s" % (self.name, self.age)

user1 = User("Feng", 18)
dict2 = {"name": "Feng", "age": 18}