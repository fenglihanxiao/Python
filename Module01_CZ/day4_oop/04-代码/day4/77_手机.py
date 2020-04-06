"""
演示手机案例
要求：
    手机电量默认是100
	打游戏每次消耗电量10
	听歌每次消耗电量5
	打电话每次消耗电量4
	接电话每次消耗电量3
	充电可以为手机补充电量
"""
# 分析
# 1. 定义类Phone
# 2. 定义变量用于描述电量值
# 3. 定义4个方法用于描述耗电操作
# 4. 定义1个方法用于描述充电操作
# 5. 运行程序，执行上述操作，观察结果
class Phone:
    def __init__(self):
        self.power = 100

    def game(self):
        """打游戏操作，耗电10"""
        print("正在打游戏，耗电10")
        self.power = self.power - 10

    def music(self):
        print("正在听歌，耗电5")
        self.power -= 5

    def call(self):
        print("正在打电话，耗电4")
        self.power -= 4

    def answer(self):
        print("正在接电话，耗电3")
        self.power -= 3

    def charge(self,num):
        print("正在充电，冲电量是%d" % num)
        self.power += num

    def __str__(self):
        return "当前手机电量为:%d" % self.power

# 创建一部电话，当前电量是100
p = Phone()
# 执行耗电操作
p.game()
print(p)
p.music()
print(p)
p.charge(8)
print(p)