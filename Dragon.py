class Dragon(object):
    def __init__(self):
        self.health = 15
        self.power = 7
        self.name = "Dragon"
        self.xp_value = 10
        self.reward = (6, 4)

    def takeDamage(self, damage):
        self.health -= damage

    def isAlive(self):
        return self.health > 0

    def display(self):
        print """                                                 /===-_---~~~~~~~~~------____
                                                |===-~___                _,-'
                 -==\\\\                         `//~\\\\   ~~~~`---.___.-~~
             ______-==|                         | |  \\\\           _-~`
       __--~~~  ,-/-==\\\\                        | |   `\        ,'
    _-~       /'    |  \\\\                      / /      \      /
  .'        /       |   \\\\                   /' /        \   /'
 /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _)   ;  ),   __--~~
                    '~~--_/      _-~/-  / \   '-~ \\
                   {\__--_/}    / \\\\_>- )<__\      \\
                   /'   (_/  _-~  | |__>--<__|      | 
                  |0  0 _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |  
                 o o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~              
                ,/|           /__>--<__/     _-~                 
             ,//('(          |__>--<__|     /                  .----_ 
            ( ( '))          |__>--<__|    |                 /' _---_~\\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/ 
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~ 
   ;'( ')/ ,)(                              ~~~~~~~~~~ 
  ' ') '( (/
    '   '  `   
"""
