class Monster(object):
    def __init__(self, name, power, health, reward):
        self.name = name 
        self.power = power
        self.health = health
        self.reward = reward

    def takeDamage(self, damage):
        self.health -= damage

    def isAlive(self):
        return self.health > 0

