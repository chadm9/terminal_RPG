from Character import Character

class Hero(Character):
    def __init__(self, name = 'Nameless'):
        super(Hero, self).__init__(name, 50, 20)
      #  self.name = name
     #   self.health = 10
     #   self.power = 5
        self.max_health = 999 
        self.magic_user = True
        self.can_miss = False
      #  self.xp = 0
      #  self.level = 1

#    def eatMushroom(self):
 #       num = random.randint(1,2)
  #      delta = random.randint(1, 10)
   #     if num > 1:
    #        self.health += delta
#            print "The mushroom was magical! Health increased by %d" % (delta)
 #       else:
  #          self.health -= delta
   #         print "The mushroom was poisoness! Health decreased by %d" % (delta)
    #    print "Your total health is now %d" % self.health





