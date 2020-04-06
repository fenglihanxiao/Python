class Father:

    def sing(self):
        print("Father single well")

    def dance(self):
        print("Father dance badly")


class Mother:

    def sing(self):
        print("Mother single badly")

    def dance(self):
        print("Mother dance well")


########################################
# If method name has collision,
# it will call first argument Father's collision method
class Child1(Father, Mother):
    pass

########################################
# If method name has collision,
# it will call first argument Mother's collision method
class Child2(Mother, Father):
    pass

ch = Child1()
ch.sing()
ch.dance()

print("******************************************")
ch2 = Child2()
ch2.sing()
ch2.dance()