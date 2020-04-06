class Phone:
    def __init__(self):
        self.power = 100

    def game(self):
        """ consume power by 10"""
        if self.power >= 10:
            print("Play game now, it is consuming power by 10")
            self.power -= 10
        else:
            print("Current battery is low, it can not used for gaming")

    def listenSong(self):
        if self.power >= 5:
            print("Listen song now, it is consuming power by 5")
            self.power -= 5
        else:
            print("Current battery is low, it can not used for listening song")

    def call(self):
        if self.power >= 4:
            print("Call someone now, it is consuming power by 4")
            self.power -= 4
        else:
            print("Current battery is low, it can not used for calling")

    def answer(self):
        if self.power >= 3:
            print("Answer someone now, it is consuming power by 4")
            self.power -= 3
        else:
            print("Current battery is low, it can not used for answering")

    def charge(self, num):
        if self.power + num > 100:
            self.power = 100
        else:
            print("Charge battery %d" % num)
            self.power += num

    def __str__(self):
        return "Current battery %d" % self.power

phone = Phone()
phone.game()
phone.game()
phone.game()
phone.game()
phone.game()
phone.game()
phone.game()
phone.game()
phone.game()
phone.game()
phone.game()
phone.game()
phone.charge(40)
phone.game()
phone.charge(80)
