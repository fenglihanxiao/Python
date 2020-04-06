"""
演示手机加强版案例
要求：
    手机耗电操作前要先判定电量是否足够完成此项任务
    手机充电操作不能充电超过最大值
"""
# 分析
# 1. 耗电操作之前必须进行判定（if系列),根据结果不同做对应的事情
# 2. 充电操作必须进行判定，手机电量不能超过最大值100

class Phone:
    def __init__(self):
        self.power = 100

    def game(self):
        """打游戏操作，耗电10"""
        # 判定当前电量是否能够完成打游戏的要求
        if self.power >= 10:
            # 正常运行，减少电量
            print("正在打游戏，耗电10")
            self.power = self.power - 10
        else:
            # 不能正常运行，不减少电量
            print("当前电量不足以完成打游戏的操作，打游戏操作被终止")

    def music(self):
        if self.power >= 5:
            # 正常运行，减少电量
            print("正在听歌，耗电5")
            self.power -= 5
        else:
            # 不能正常运行，不减少电量
            print("当前电量不足以完成听歌的操作，听歌操作被终止")

    def call(self):
        if self.power >= 4:
            # 正常运行，减少电量
            print("正在打电话，耗电4")
            self.power -= 4
        else:
            # 不能正常运行，不减少电量
            print("当前电量不足以完成打电话的操作，打电话操作被终止")

    def answer(self):
        if self.power >= 3:
            # 正常运行，减少电量
            print("正在接电话，耗电3")
            self.power -= 3
        else:
            # 不能正常运行，不减少电量
            print("当前电量不足以完成接电话的操作，接电话操作被终止")

    def charge(self,num):
        # 判断当前电量，再与充电量做比较，根据情况执行不同的内容
        if self.power + num > 100:
            # 过冲
            print("充电操作提前结束，当前电量为：100")
            self.power = 100
        else:
            # 正常冲
            print("正在充电，冲电量是%d" % num)
            self.power += num

    def __str__(self):
        return "当前手机电量为:%d" % self.power

# 创建一部电话，当前电量是100
p = Phone()
# 执行耗电操作
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
print(p)
p.game()
p.charge(40)
print(p)
p.game()
print(p)
p.charge(80)
print(p)