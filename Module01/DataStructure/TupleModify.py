class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name=%s;Age=%s" % (self.name, self.age)

tuple1 = (18, "itcast", User("Richard", 44), User("Amy", 32))

############################################################
# If it is a object, it allow write on obj.member_var
tuple1[2].age = 18

for data in tuple1:
    print(data)


