import random
class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health 
        self.power = power 

    def isAlive(self):
        return self.health > 0

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





