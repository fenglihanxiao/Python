"""
演示成员方法调用成员
"""
class Cat:
    def catch(self):
        # 1.跳起
        # 2.抓住
        # 3.咬死
        self.jump()
        self.grasp()
        self.bite()

    def jump(self):
        print("猫跳起来")

    def grasp(self):
        print("猫抓住了老鼠")

    def bite(self):
        print("猫咬住了老鼠")

cat1 = Cat()
cat1.catch()
