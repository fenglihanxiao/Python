"""
演示鸭子类型
"""
class Teacher:
    def teach(self):
        print("教授知识")

class Man(Teacher):
    def teach(self):
        print("教授Python知识")

class GamePlayer:
    def teach(self):
        print("教玩游戏")

class Demo:
    def dothing(self,teacher):
        # 来一个老师教我做
        teacher.teach()

d = Demo()
# man = Man()
player = GamePlayer()
d.dothing(player)