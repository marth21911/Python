#class - attributes and methods





class SuperHero:
    #this is the constructor- blueprint of attributes
    def __init__(self, name, ability, costume):
        self.name = name
        self.ability = ability
        self.costume = costume 
        self.health = 100 
        self.attack_power = 3
        #nemesis
        #sidekick



    #down here will be  our methods
    #hero introduction
    def intro(self):
        print (f"Hi my name is {self.name}, my super power is {self.ability}. I like wearing {self.costume}")
        return self

#method for fighting
    def fight(self, target):
        #Logic for attribute effects
            target.health -= self.attack_power
        print(f"{self.name} is using {self.ability} to fight {target.name}!!
        {target.name} is now {target.health}")




    #Make stuff happen down here
    super_hero1 = SuperHero("AxeMan", "Giant Axe", "Axeless Chaps")
    super_hero2= SuperHero ("KeysMaster", "Key Ring", "Key Chain Mail")
    super_hero3=SuperHero ("Home Bass", "The Thump", "Bassic Boots")

    super_hero1.intro()
    super_hero2.fight(super_hero3)