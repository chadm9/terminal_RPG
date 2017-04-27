import os
from Hero import Hero
from Demigod import Demigod
from Wizard import Wizard
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
    wait()
    return monsters


def initializeHero():

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
    print '************************************************'
    wait()
    name = raw_input("What is thy name brave wanderer?\n> ")
    selection = raw_input("""What art though?
1. A Warrior 
2. A Wizard
3. A Demigod
> """)
    if selection == "1":
        return Hero(name)
    elif selection == "2":
        return Wizard(name)
    else:
        return Demigod(name)
    

def printVictory(hero):
    print "%s, you have slain all foes and are victorius!" % (hero.name)
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
    print "                     Y O U  A R E  D E A D"
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

def cast_spell(monster, hero):
    spell = random.randint(0,3)
    if spell == 0:
        print "You cast a spell of weakening, your enemy's power has decreased by 5."
        monster.power -= 5
        print "%s's power is now %d" % (monster.name, monster.power)
    elif spell == 1:
        print "You cast an attack spell, your enemy's health has decreased by 5."
        monster.health -= 5
        print "%s's health is now %d" % (monster.name, monster.health)
    elif spell == 2:
        print "You have woven a powerful magic, your enemy's health and power decreased by 5."
        monster.power -= 5
        monster.health -= 5
        print "%s's power is now %s and its health is now %s." % (monster.name, monster.power, monster.health)
    elif spell == 3:
        print "Your enemy resisted your magical attack."
    hero.health -=  1
    print "You have %d health remaining" % (hero.health)
    wait()

def attack(attacker, defender):
    if attacker.can_miss:
        bound = 0
    else:
        bound = 1
    outcome = random.randint(bound,2)
    if outcome == 0:
        print "%s dodged %s's attack" % (defender.name, attacker.name)
    elif outcome == 1:
        print "%s landed a glancing blow on %s" % (attacker.name, defender.name)
    elif outcome == 2:
        print "%s struck down on %s with a mighty blow" % (attacker.name, defender.name)

    return attacker.power * outcome

def displayMatchup(hero, monster):
    print "\n%s, you have encountered a %s" % (hero.name, monster.name)
    print "You have %d health and %d power." % (hero.health, hero.power)
    print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
    monster.display()
    wait()

def monsterActs(hero, monster):
    selection = random.randint(1, 7)
    if selection == 1:
        print "%s does nothing." % (monster.name)
        wait()
    elif selection > 1 and selection <=3:
        print "The %s ran away..." % (monster.name)
        wait()
        return "battle_over" 
    else:
        print "%s attacks" % (monster.name)
        hero.health -= attack(monster, hero) 
        print "You have %d health remaining." % (hero.health)
        wait()

def checkResult(hero, monster, monsters):
    if not hero.isAlive():
        printDeath()
        exit()
    if not monster.isAlive():
        print "You have defeated the %s!" % monster.name
        hero.health += monster.reward[0]
        hero.power += monster.reward[1]
        print "You power has increased to %s and your health to %s" % (hero.power, hero.health)
        del monsters[monsters.index(monster)]
        wait()
        wait()
        return "battle_over" 
    if hero.isAlive() and hero.health < 5 and hero.power < 8:
        print "You have gone into a rage.  Your power has increased by three!"
        hero.power += 3

def heroActs(hero, monster):
    mushroom = random.randint(0,1)
    print "What do you want to do now?"
    print "1. fight" 
    print "2. flee"
    print "3. check inventory"

    if hero.magic_user == True:
        print "4. cast spell"
    print "> ",
    user_input = raw_input()

    if user_input == "1":
        print "Attacking..."
        wait()
        monster.health -= attack(hero, monster)
        print "%s has %s health remaining." % (monster.name, monster.health)
        wait() 
    elif user_input == "3":
        checkInventory(hero) 

    elif user_input == "2":
        print "You ran away..."
        wait()
        return "battle_over" 
    elif user_input == "4" and hero.magic_user == True:
        print"Casting spell...."
        wait()
        cast_spell(monster, hero)
    else:
        print "Invalid input. The opportunity for action has been lost..."

def generateLocation():
    location = random.randint(1,2)
    if location == 1:
        print """           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`"""
        print "You find yourself on a warm beach."

    elif location == 2:
        print """                                  _
                        .-.      / \\        _
            ^^         /   \\    /^./\\__   _/ \\
          _        .--'\\/\\_ \\__/.      \\ /    \\  ^^  ___
         / \\_    _/ ^      \\/  __  :'   /\\/\\  /\\  __/   \\
        /    \\  /    .'   _/  /  \\   ^ /    \\/  \\/ .`'\\_/\\
       /\\/\\  /\\/ :' __  ^/  ^/    `--./.'  ^  `-.\\ _    _:\\ _
      /    \\/  \\  _/  \\-' __/.' ^ _   \\_   .'\\   _/ \\ .  __/ \\
    /\\  .-   `. \\/     \\ / -.   _/ \\ -. `_/   \\ /    `._/  ^  \\
   /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
 @/        `.  / /      `-.   /  .-'   / .   .'   \\    \\  \\  .-  \\%
 @(88%@)@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
 @88:::&(&8&&8::JGS:&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
 `::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8::::::'
  `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::' """
        print "You are on a mountainous terrain"

def generateEvent(wandering):
    event = random.randint(1, 21)
    if event <= 7:
        print "You sense an ominous presence."
    elif event > 7 and event <= 14:
        print "You see nothing on the horizon."
    elif event == 15:
        print "An elixir of healing is hidden under some brush."
    elif event == 16:
        print "A root of power is planted at your feet."
    else:
        print "Wild mushrooms are growing in the area."
    return event 
        
def getReaction(event, hero):
    print "Enter an action.\n1. press onward\n2. check inventory"
    if event > 14:
        print "3. pick up item"
    selection = raw_input("> ") 

    if event > 14 and selection == "3":
        if event == 15:
            hero.elixir_count += 1
            print "You picked up the elixir."
            wait()
        if event == 16:
            hero.root_count += 1
            print "You picked up the root."
            wait()
        if event > 16:
            print "You picked up a mushroom."
            wait()
            hero.mushroom_count += 1

    if selection == "2":
        checkInventory(hero)
    wait()

def checkInventory(hero):
    print "\n%s elixirs of life" % (hero.elixir_count)
    print "%s roots of power" % (hero.root_count)
    print "%s wild mushrooms\n" % (hero.mushroom_count)
    print "1. use elixir"
    print "2. use root"
    print "3. use mushroom"
    print "4. exit inventory\n"

    selection = raw_input("What do you want ot do?\n> ")

    if selection == "1":
        if hero.elixir_count > 0:
            hero.health += 3
            hero.elixir_count -= 1
            print "You used an elixir, your health is increased to %s" % (hero.health)
        else:
            print "You have no elixirs..."


    if selection == "2":                       
        if hero.root_count > 0:
            hero.power += 2
            hero.root_count -= 1
            print "You used a root, your health is increased to %s" % (hero.power)
        else:
            print "You have no roots.."

    if selection == "3":                       
        if hero.mushroom_count > 0:
            hero.eatMushroom() 
            hero.mushroom_count -= 1
        else:
            print "You have no elixirs..."
 

def main():

    hero = initializeHero()          #Select the hero's character and name.
    monsters = generateFoes(hero)    #Randomly initialize a user selected number of monsters.
    
    while len(monsters) > 0:   #While there are monsters to fight.

#        wandering = True
 #       while wandering:
 #           generateLocation()
 #           event = generateEvent(wandering)
 #           getReaction(event, hero)
 #           if event <= 7:
 #               break

        for monster in monsters:

            wandering = True
            while wandering:
                generateLocation()
                event = generateEvent(wandering)
                getReaction(event, hero)
                if event <= 7:
                    break

            displayMatchup(hero, monster)       #Print the hero's and monster's stats for comparison

            while monster.isAlive() and hero.isAlive():
                if random.randint(0,1):                  #Determine who attacks first.
                    print "%s is first to act" % (monster.name)
                    wait()
                    if monsterActs(hero, monster) == "battle_over": break
                    if checkResult(hero, monster, monsters) == "battle_over": break
                    if heroActs(hero, monster) == "battle_over": break
                    if checkResult(hero, monster, monsters) == "battle_over": break
 
                else:
                    print "%s is first to act" % (hero.name)
                    wait()
                    if heroActs(hero, monster) == "battle_over": break
                    if checkResult(hero, monster, monsters) == "battle_over": break
                    if monsterActs(hero, monster) == "battle_over": break
                    if checkResult(hero, monster, monsters)  == "battle_over": break

    printVictory(hero)   #All monsters are dead.

main()
