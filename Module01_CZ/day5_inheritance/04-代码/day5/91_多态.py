"""
演示多态
"""
class Teacher:
    def teach(self):
        print("教授知识")

class Driver:
    def drive(self):
        print("开车")

class Man(Teacher,Driver):
    def teach(self):
        print("教授Python知识")
    def drive(self):
        print("开小轿车")

class Demo:
    def play(self,driver):
        driver.drive()

    def study(self,teacher):
        teacher.teach()

# 方案一：创建司机对象
d = Driver()
# 方案二：创建了一个具有司机特征的对象
man = Man()
demo = Demo()
demo.play(man)
demo.study(man)