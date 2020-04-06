class Teacher:
    def teach(self):
        print("Teach students")


class Man(Teacher):
    def teach(self):
        print("Teach python class")


class GamePlayer:
    def teach(self):
        print("Teach how to play games")


class Demo:
    def do_thing(self, teacher):
        teacher.teach()

demo1 = Demo()
man = Man()
demo1.do_thing(man)

print("===================================")

############################################
# Object satisfy the same member variable and
# method. They both have the same method teach()
# instead of multiple inheritance relationship
# type matching, they have a number of characters
#   1. Functional method or member variable are
#      consistent for weak type
#   2. Special polymorphic
demo2 = Demo()
player = GamePlayer()
demo1.do_thing(player)