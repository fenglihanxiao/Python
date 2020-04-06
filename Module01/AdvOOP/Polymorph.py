class Teacher:
    def teach(self):
        print("Teach students")


class Driver:
    def drive(self):
        print("Drive a car")


class Man(Teacher, Driver):
    def teach(self):
        print("Teach python class")

    def drive(self):
        print("Drive a BMW race car")


class Demo:
    def play(self, driver):
        driver.drive()


    def study(self, teacher):
        teacher.teach()

#############################################
# First way without polymorphic
dr = Driver()
demo1 = Demo()
demo1.play(dr)

print("=============================================")

#############################################
# Second way by adopting polymorphic
#############################################
man = Man()
demo2 = Demo()
demo2.play(man)
demo2.study(man)