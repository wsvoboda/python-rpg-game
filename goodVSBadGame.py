from random import randint # to be able to generate a random number for the attack
from gameMessages import *

class Character: 
    def __init__(self, name, defense, power, lifePoints):
        self.name = name
        self.defense = defense
        self.power = power
        self.lifePoints = lifePoints

    def takeDamage(self):
        damageDone = randint(0,5) - (self.defense//10)
        if damageDone <= 0:
            print(f"The troll attacked but missed! You didn't lose any health points.")
        else:
            self.lifePoints -= damageDone
            print(f"The troll attacked! You lost {damageDone} health points.\n")

class Troll(Character):
    def takeDamage(self):
        damageDone = randint(0,7) + ((goodGuy.power)//10)
        if damageDone <= 0:
            print(f"Your attacked missed! The troll didn't lost any health points.")
        else:
            self.lifePoints -= damageDone
            print(f"\nYou attacked the troll! It lost {damageDone} health points.")

goodGuy = welcomeMessage()
troll = Troll("Troll", 20, 20, 20)
battleOptionScreen()

while goodGuy.lifePoints > 0 and troll.lifePoints > 0:
    battleOptionScreen()

if goodGuy.lifePoints <= 0:
    print(f"""
            -|-
             |
         .-'~~~`-.
       .'         `.
       |  R  I  P  |
       |           |
       |           |
     \\\\|           |//
  ^^^^^^^^^^^^^^^^^^^^^^^
  You died, {goodGuy.name}.""")
else:
    print(f"""
       _      _                   
      (_)    | |                  
__   ___  ___| |_ ___  _ __ _   _ 
\ \ / / |/ __| __/ _ \| '__| | | |
 \ V /| | (__| || (_) | |  | |_| |
  \_/ |_|\___|\__\___/|_|   \__, |
                             __/ |
                            |___/ 

You defeated the troll, {goodGuy.name}! Amazing!""")

### testing things below here ###

# ideas

# include ascii images 

# include a defense parameter
    # defense of 10 = reduces attack by 1 unit (instead of attacking 5, will attack 4)
    # defense of 20 = reduces attack by 2 units (instead of attacking 5, will attack 3)
    # etc

# include a power parameter
    # power of 10 = increases attack by 1 unit
    # power of 20 = increases attack by 2 units
    # etc

# provide option of 3 characters

# cherry = Character("Cherry", 30, 30, 20)
# mango = Character("Mango", 20, 50, 20)
# peach = Character("Peach", 50, 20, 20)

# print(cherry, mango, peach)

# dice roll to determine stats

# have option of 3 enemies (chosen a random)



