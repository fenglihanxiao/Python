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
import random
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
        flowers = ("♠","♥","♣","♦")
        nums = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
        kings = {"big":"大王","small":"小王"}
        for flower_ in flowers :
            for num_ in nums:
                p = Poke(flower_,num_)
                cls.pokes.append(p)
        cls.pokes.append(Poke(kings["big"],""))
        cls.pokes.append(Poke(kings["small"], ""))

    #洗牌
    @classmethod
    def wash(cls):
        # 洗牌是从牌堆中找出一张固定的牌，与随机的一张牌交换位置
        # 迭代牌堆，找出一张牌
        # 产生随机数，作为被交换牌
        # 交换
        for idx in range(54):
            idxx = random.randint(0,53)
            cls.pokes[idx],cls.pokes[idxx] = cls.pokes[idxx],cls.pokes[idx]

    #发牌
    @classmethod
    def send_poke(cls):
        pass

    # 临时方法：展示牌堆
    @classmethod
    def show(cls):
        for poke in cls.pokes:
            print(poke ,end=" ")
        print()

Poke.init_pokes()
Poke.show()
Poke.wash()
Poke.show()

