"""
案例：演示鸭子类型的成员变量调用
"""
class Teacher:
    def __init__(self,name):
        self.name = name

class Cat:
    def __init__(self,name):
        self.name = name

def speak(teacher):
    print(teacher.name)

# 步骤一：请演示程序
t1 = Teacher("张教授")
# 注意：speak函数中需求老师Teacher对象，传入teacher正常执行
speak(t1)

# 步骤二：请演示程序
# 注意：如果传入c1对象，仅仅是语法上满足Cat类有name属性，此时运行满足鸭子类型（属性满足鸭子类型）
# c1 = Cat("大帅")
# speak(c1)