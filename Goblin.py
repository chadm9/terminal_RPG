class Goblin(object):
    def __init__(self):
        self.health = 5
        self.power = 2
        self.name = 'Goblin'
        self.xp_value = 5
        self.reward = (4, 2)

    def takeDamage(self, damage):
        self.health -= damage

    def isAlive(self):
        return self.health > 0

    def display(self):
        print '''
                        _.-=/^---._
                      /^_.-^  _  --^=_
                   ./'-^__    _>=\^^==^-.   
                   |'/^^_/  /^    \ \.^\\\\\/\\
                  ,|/| '  /'  _____\ `\|.^.|
                  |'/   /_--^^ .   ^^-./ /||
                  |/,--^  ,     |     / /||'
                ._|/   \ /  __,-/    / /-,||
                \ '/    ;  /O  / _    |) )|,
                 i \./^O\./_,-^/^    ,;-^,'      
                  \ |`--/ ..-^^      |_-^       
                   `|  \^-_,/^Y\      | ^^\    
                   _i.  \\".--V_/     /| \. ^\._____...--.>^^^^^^-------...._
                  /  i   ^--^^     /'|' |\. |./'        |                  ;
___...----/^^^^---|.  `._\  /^   /' |'_/' \ `|         |'               ,/'
         |'        \   _|^-.__./'__.^^\     .|        ,|            _.-^
         `\       ,|`_./^^-----^^._    ` ./ /        /^        _.-^^/
                  |'  ^                  /-^                ./^    /
\                 `\_     __.-<       _,/                 ./'     |'
 `\.        `i       ^^--/._____...--^            .      ./       |.
   `|        |                                   /       /        `|'''
