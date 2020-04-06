import random

class Person:
    def __init__(self, name):
        self.name = name
        self.life = 100

    def __str__(self):
        state = ""
        if self.life == 100:
            state = "No hurst"
        elif self.life >= 70 and self.life < 100:
            state = "Light hurst"
        elif self.life >= 1 and self.life < 70:
            state = "Serious hurst"
        elif self.life <= 0:
            state = "Dead"
        return "%s's life value:%s" % (self.name, state)


class Hero(Person):
    def fire(self, ter):
        damage = random.randint(20, 50)

        hit_ratio = random.randint(1, 100)

        if ter.life == 0:
            print("********* %s is dead, do not shot body" % ter.name)
        else:
            if hit_ratio > 20:
                print("%s shoot %s, cause %d damage" % (self.name, ter.name, damage))
                if ter.life < damage:
                    ter.life = 0
                else:
                    ter.life -= damage
            else:
                print("******* Not a good hero shot.")


class Terrist(Person):
    def fire(self, hero):
        damage = random.randint(5, 15)

        hit_ratio = random.randint(1, 100)
        if hit_ratio > 60:
            print("%s shoot %s, cause %d damage" % (self.name, hero.name, damage))
            if hero.life < damage:
                self.life = 0
            else:
                hero.life -= damage
        else:
            print("======== %s Not a good terrist shot." % self.name)


def main():
    hero = Hero("Feng")
    ter1 = Terrist("James")
    ter2 = Terrist("Alex")
    ter3 = Terrist("Tony")
    ters = []
    ters.append(ter1)
    ters.append(ter2)
    ters.append(ter3)

    while True:
        id = random.randint(1, 3)
        if id == 1:
            hero.fire(ter1)
        elif id == 2:
            hero.fire(ter2)
        elif id == 3:
            hero.fire(ter3)

        for t in ters:
            t.fire(hero)

        print(hero)
        print(ter1)
        print(ter2)
        print(ter3)
        print()

        if hero.life <= 0:
            print("Hero:%s is dead;life=%d" % (hero.name, hero.life))
            break

        if ter1.life <= 0 and ter2.life <= 0 and ter3.life <= 0:
            print("All Terrist is dead;life=%d" % (ter1.life))
            break

main()