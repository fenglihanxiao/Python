import random

class Poker:
    pokers = []
    player1 = []
    player2 = []
    player3= []
    lasts = ()

    def __init__(self, flower, num):
        self.flower = flower
        self.num = num

    def __str__(self):
        return "%s:%s" % (self.flower, self.num)

    @classmethod
    def init_poker(cls):
        flowers = ("Black Heart", "Red Heart", "Cherry Blossom", "Squid")
        nums = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        kings = {"big": "Big King", "small": "Small King", }

        for _flower in flowers:
            for _num in nums:
                p = Poker(_flower, _num)
                """ Because it is a class method, it has to use cls.method """
                cls.pokers.append(p)

        cls.pokers.append(kings["big"])
        cls.pokers.append(kings["small"])

    @classmethod
    def shuffle(cls):
        """
            1. Get one fixed slut and swap with random index
            2. Iterate pokers to find poker
            3. Generate random index
            4. swap the poker

        :return void:
        """
        for idx in range(54):
            idxx = random.randint(0, 53)
            ########################################################
            # Swap two element in python way
            cls.pokers[idx],cls.pokers[idxx] = cls.pokers[idxx], cls.pokers[idx]

    @classmethod
    def distribute_poker(cls):
        for _ in range(17):
            p = cls.pokers.pop(0)
            cls.player1.append(p)

            p2 = cls.pokers.pop(0)
            cls.player2.append(p2)

            p3 = cls.pokers.pop(0)
            cls.player3.append(p3)
        """
            1. Make sure use cls.lasts instead of lasts, it is a local variable
        """
        cls.lasts = tuple(cls.pokers)

    @classmethod
    def show_pokers(cls):
        for p in cls.pokers:
            print(p, end=" ")
        print()

    @classmethod
    def show_players(cls):
        print("=============================== Player1:%d" % cls.player1.__len__(), end="->")
        for i in cls.player1:
            print(i, end=" ")
        print()
        print("=============================== Player2:%d" % cls.player2.__len__(), end="->")
        for i in cls.player2:
            print(i, end=" ")
        print()
        print("=============================== Player3:%d" % cls.player3.__len__(), end="->")
        for i in cls.player3:
            print(i, end=" ")
        print()
        print("=============================== Last:%d" % cls.lasts.__len__(), end="->")
        for i in cls.lasts:
            print(i, end=" ")
        print()

def main():
    Poker.init_poker()
    # Poker.show_pokers()
    Poker.shuffle()
    # Poker.show_pokers()
    Poker.distribute_poker()
    # Only left three cards
    Poker.show_pokers()

    Poker.show_players()

main()