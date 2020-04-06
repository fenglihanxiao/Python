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
    def sing(self):
        print("Child love to sing well")
        ########################################
        # If method name has collision,
        # Call collision method by class name specifier
        Father.sing(self)
        Mother.sing(self)


ch = Child1()
ch.sing()
