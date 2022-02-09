# Class - Attributes - Methods





class SuperHero:

    population = 0


    # This is the constructor - blueprint of attributes
    def __init__(self, name, ability, suit, health = 100, attack_power = 3):
        self.name = name
        self.ability = ability
        self.suit = suit
        self.health = health
        self.attack_power = attack_power
        SuperHero.population += 1
        # nemisis
        # sidekick

    #  Class Methods -
    @classmethod
    def printPopulus(cls):
        print(f"Super Hero population is currently: {SuperHero.population}")

    # Down here will be our Methods

    #Let's make a method to introduce our Heroes!!
    def intro(self):
        print(f"Hi, my name is {self.name}, my super power is {self.ability}. I like wearing {self.suit}")
        return self

    # Method for fighting/ superheros have gon crazy fighting eachother
    def attack(self, target):
        # Logic to change attributes during the attack
        print(target.health)
        if target.health < self.attack_power:
            print(f"You cannot tacky tack {target.name} because they got slept!")
        else:
            target.health -= self.attack_power
            print(f"{self.name} is using {self.ability} to hurt {target.name}! {target.name}'s health is now {target.health}")
        return self

    def train(self, numOfDays):
        self.attack_power += (2 * numOfDays)
        print(f"{self.name} went to the Dojo for training! Increased attack power to {self.attack_power}!")
        return self
# Make our stuff happen down here

super_hero1 = SuperHero("Jim", "Making Slim Jims", "Overalls")
super_hero2 = SuperHero("Felix", "CSS Reducinizing", "Gold Plated Armour")
super_hero3 = SuperHero("Rafaelalangelo", "The Power of 2 Turtles", "Just a headband")
super_hero4 = SuperHero("Rafaelalangelo", "The Power of 2 Turtles", "Just a headband")
super_hero5 = SuperHero("Rafaelalangelo", "The Power of 2 Turtles", "Just a headband")



super_hero1.intro()
super_hero2.attack(super_hero3)
super_hero2.attack(super_hero3)
super_hero2.train(7).attack(super_hero3)
super_hero1.printPopulus()
SuperHero.printPopulus()
# super_hero3.intro()
