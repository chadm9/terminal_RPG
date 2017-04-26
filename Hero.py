import random

class Hero(object):
    def __init__(self, name = 'Nameless'):
        self.name = name
        self.health = 10
        self.power = 5
        self.max_health = self.health
        self.xp = 0
        self.level = 1

    def cheer_hero(self):
        print 'Fight hard, %s' % self.name

    def isAlive(self):
        return self.health > 0

    def attack(self, who):
        who.health -= self.power

    def increaseHealth(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def checkLevel(self):
        if self.xp > 3:
            self.level = 2
            self.level_up()

    def levelUp(self):
        self.max_health += 10
        self.health = self.max_health
        self.power += 5

    def eatMushroom(self):
        num = random.randint(1,2)
        delta = random.randint(1, 10)
        if num > 1:
            self.health += delta
            print "The mushroom was magical! Health increased by %d" % (delta)
        else:
            self.health -= delta
            print "The mushroom was poisoness! Health decreased by %d" % (delta)
        print "Your total health is now %d" % self.health





