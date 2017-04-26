from Hero import Hero
from Vampire import Vampire
from Dragon import Dragon
from Goblin import Goblin
import random
import time



def generateFoes(hero):
    monsters = []
    number_of_monsters = int(raw_input("Welcome %s, how many monsters will you fight?\n> " % (hero.name)))
    for i in range(number_of_monsters):
        random_int = random.randint(1, 3)
        if random_int == 1:
            monsters.append(Goblin())
        elif random_int == 2:
            monsters.append(Vampire())
        elif random_int ==3:
            monsters.append(Dragon())

    return monsters


def startGame():

    print '************************************************'
    print '*           M O N S T E R  Q U E S T           * '
    print '************************************************'
    print """                                .-.
                               {{@}}
               <>               8@8
             .::::.             888
         @\\\\/W\/\/W\//@         8@8
          \\\\/^\/\/^\//     _    )8(    _
           \_O_<>_O_/     (@)__/8@8\__(@)
      ____________________ `~"-=):(=-"~`
     |<><><>  |  |  <><><>|     |.|
     |<>      |  |      <>|     |S|
     |<>      |  |      <>|     |'|
     |<>   .--------.   <>|     |.|
     |     |   ()   |     |     |P|
     |_____| (O\/O) |_____|     |'|
     |     \   /\   /     |     |.|
     |------\  \/  /------|     |U|
     |       '.__.'       |     |'|
     |        |  |        |     |.|
     :        |  |        :     |N|
      \<>     |  |     <>/      |'|
       \<>    |  |    <>/       |.|
        \<>   |  |   <>/        |K|
         `\<> |  | <>/'         |'|
           `-.|  |.-`           \ /
              '--'               ^"""
    return Hero(raw_input("What is thy name brave hero?\n> "))

def printVictory():
    print """\n\n
                     .-'`-.
                    / | |  \\
                   /  | |   \\
                  |___|_|__  |                T H E  R E A L  M O N S T E R  IS  Y O U . . .  
                  ||<o>| <o>`|
                  ||   J_   )|
                  `|`-'__`-'|/
                   |  `--'  |
                 .-|        |_
              .-'  \     /  | |`-.
           .-'      `.     /| |   \\
          /           ````' | |    \\
         |_____             | |     L
      .-' ___   `-.         F F  |  |    ||`-.___
    .'.-'  |  `-.  `.      J J   /  |    ||    _.>
   / /|    |    |`.  \     | |   |/ |    ||_.-'
  / / |    |    |  `. `.   F F   |  |==============================
 J /  |    |    |    \  L J J    |  |      `:::::::.       `:::::::.
 FJ   |    |    |    |L J/ /     |   \       :::::::.        :::::::\\
J |() | () | () | () | J L/      |   |        :::::::         :::::::L
| F   | .-'_ \  |    |  LJ       | /  L       ::::::::        :::::::J
| L   | /    \\\\ |    |  | L      |    |       ::::::::        ::::::::L
| L   ||     ):||    |  | |     /|     L      ::::::::        ::::::::|
J |   ||:._.'::||    |  | |----' |     |      ::::::::        ::::::::|     .---.
J |   |J:::::::||    |  | |    _/\     |      ::::::::        ::::::::|    /(@  o`.
 LJ   | \:::::/ |    |  | |---'\  |    |      ::::::::        ::::::::|   |    /^^^
 J L  |  `-:-'  |    |  | F  | \  |    J      ::::::::        ::::::::|    \ . \\vvv
  LJ()| () | () | () |  F F  |  \  \--._L     ::::::::        ::::::::|     \ `--'
  J \ |    |    |    | J J     \    |  |      ::::::::        ::::::::|      \ `.
   \ \|    |    |    | / /    |     |  |      ::::::::        ::::::::|       L  \\
    \ \    |    |    |/ /|     |    | .-'|    ::::::::        ::::::::|       |   \\
     `.`.  |    |   .'.' |     |    |/ /`L    ::::::::        ::::::::|       |    L
     | `.`-.____|.-'.-'  |     |    | <`. \   ::::::::        ::::::::|       |    |
     | | `-.______.-'    |    \|    |_`::\ `. ::::::::        ::::::::|       F    |
     | J\ |  |           |     |    /:  \::. \::::::::        ::::::::F      /     |
     |  L\|--|           |     _.--|::   `::\ `.::::::       .:::::::J      /      F
     J  J |\\\\|-.____     |__.-'    |:      \::. \::::        ::::::::F    .'      J
      L  \| >||      `--' J        |'      .`::\ `.:'      .::::::::/   .'        F
      J   |//JJ        |   L       |---.   .--\::. \---.   .---.   <---<         J
       L  |< |J        |\=/|       ( _  \=/  _ `::\ `.  \=/  _  \=/  _  \       /
       J  |\\\\|J        | | /        )_)  |  (_)  \::. \  |  (_)  |  (_)  |     /
        \ |--|J        |//\\\\       /    //\     //`::\ `./\     //\     /    .'
         \|  |L `      )/  )` `' '|`---//  `---//  `\::. \ `---//  `---'   .'
VK________|  L_\    '  /___/ ' |  |___//______//_____`::\ |___//_________.'_________
          F  F J``  -'|    | | |  |                    \:_|
         

"""


def printDeath():
    print '''                       .ed"""" """$$$$be.                     
                     -"           ^""**$$$e.                  
                   ."                   '$$$c                 
                  /                      "4$$b                
                 d  3                     $$$$                
                 $  *                   .$$$$$$               
                .$  ^c           $$$$$e$$$$$$$$.              
                d$L  4.         4$$$$$$$$$$$$$$b              
                $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$              
    e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$              
   z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c  
  4$$$$L   \     $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$. 
  ^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$ 
    "**$$$ec   "\   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P"" 
          "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"   
            ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"         
               "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"           
                 "*$$$  *=%4.$ L L$ P3$$$F $$$P"              
                    "$   "%*ebJLzb$e$$$$$b $P"                
                      %..      4$$$$$$$$$$ "                  
                       $$$e   z$$$$$$$$$$%                    
                        "*$c  "$$$$$$$P"                      
                         ."""*$$$$$$$$bc                      
                      .-"    .$***$$$"""*e.                   
                   .-"    .e$"     "*$c  ^*b.                 
            .=*""""    .e$*"          "*bc  "*$e..            
          .$"        .z*"               ^*$e.   "*****e.      
          $$ee$c   .d"                     "*$.        3.     
          ^*$E")$..$"                         *   .ee==d%     
             $.d$$$*                           *  J$$$e*      
              """""                             "$$$"   
'''

def wait():
    print '.',
    time.sleep(0.6)
    print '.',
    time.sleep(0.6)
    print '.',
    time.sleep(0.6)
    print '.',
    time.sleep(0.6)
    print '.\n'

def attack(attacker, defender):
    outcome = random.randint(0,2)
    if outcome == 0:
        print "%s dodged %s's attack" % (defender.name, attacker.name)
    elif outcome == 1:
        print "%s landed a glancing blow on %s" % (attacker.name, defender.name)
    elif outcome == 2:
        print "%s struck down on %s with a mighty blow" % (attacker.name, defender.name)

    return attacker.power * outcome

def main():

    hero = startGame()

    monsters = generateFoes(hero)
    wait()

    while len(monsters) > 0:

        for monster in monsters:
            print "\n%s, you have encountered a %s" % (hero.name, monster.name)
            print "You have %d health and %d power." % (hero.health, hero.power)
            print "The %s has %d health and %d power.\n" % (monster.name, monster.health, monster.power)
            monster.display()


            while monster.isAlive() and hero.isAlive():

                wait()
                monster_acts_1st = random.randint(0,1)
                if monster_acts_1st:
                    print '%s is first to act' % (monster.name)
                    wait()
                    monster_attacks = random.randint(1,3)
                    if monster_attacks > 1:
                        print "%s attacks" % (monster.name)
                        hero.health -= attack(monster, hero)
                        print "You have %d health remaining." % (hero.health)
                        if not hero.isAlive():
                            print "                     Y O U  A R E  D E A D"
                            printDeath()
                            exit()
                    else:
                        print 'The %s ran away...' % (monster.name)
                        wait()
                        break

                else:
                    print "%s is first to act" % (hero.name)

                mushroom = random.randint(0,1)
                #print "You have %d health and %d power." % (hero.health, hero.power)
                #print "The %s has %d health and %d power.\n" % (monster.name, monster.health, monster.power)
                print "What do you want to do?"
                print "1. fight %s" % monster.name
                if mushroom == True:
                    print "2. flee"
                    print "3. eat a wild mushroom"
                else:
                    print "2. flee"
                print "> ",
                user_input = raw_input()

                if user_input == "1":
                    print "Attacking..."
                    wait()
                    monster.health -= attack(hero, monster)
                    print "%s has %s health remaining." % (monster.name, monster.health)
                    wait()
                    if monster.health <= 0:
                        print "You have defeated the %s!" % monster.name
                        hero.health += monster.reward[0] 
			hero.power += monster.reward[1] 
                        print "You power has increased to %s and your health to %s" % (hero.power, hero.health)
                        del monsters[monsters.index(monster)]
                        wait()
                        wait()

                elif user_input == "3" and mushroom == True:
                    print 'Eating Mushroom...'
                    wait()
                    hero.eatMushroom()
                    if not hero.isAlive():
                        print "                     Y O U  A R E  D E A D"
                        printDeath()
                        exit()

                elif user_input == "2":
                    print 'Fleeing...'
                    wait()
                    print "You ran away..."
                    wait()
                    break

                else:
                    print "Invalid input %s" % user_input

                if monster.health > 0 and random.randint(1,3) > 1:
                    print "%s attacking..." % (monster.name)
                    wait()
                    hero.health -= attack(monster, hero)
                    print "You have %d health remaining." % (hero.health)
                    if not hero.isAlive():
                        print "                     Y O U  A R E  D E A D"
                        printDeath()
                        exit()
                elif monster.health > 0:
                    wait()
		    print "%s ran away" % (monster.name)
                    wait()
		    break

                if hero.isAlive() and hero.health < 5:
                    print "You have gone into a rage.  Your power has increased!"
                    hero.power += 5

    print "%s you have slain all foes.  You are victorius!" % (hero.name)
    printVictory()

main()
