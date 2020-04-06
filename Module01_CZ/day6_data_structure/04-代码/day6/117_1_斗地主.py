"""
案例斗地主
分析：
1.扑克牌作为对象呈现
2.创建未发牌的牌堆的列表
3.创建三个玩家牌堆的列表
4.创建底牌的元组
5.最原始的牌堆初始化，将54张牌加入到牌堆
6.创建洗牌操作
7.创建发牌操作
"""
class Poke:
    pokes = []
    player1 = []
    player2 = []
    player3 = []
    def __init__(self,flower,num):
        self.flower = flower
        self.num = num

    def __str__(self):
        return "%s%s" % (self.flower,self.num)

    # 初始化牌
    @classmethod
    def init_pokes(cls):
        pass

    #洗牌
    @classmethod
    def wash(cls):
        pass

    #发牌
    @classmethod
    def send_poke(cls):
        pass


