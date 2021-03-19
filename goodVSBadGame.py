from random import randint
from dice_roll import *


class Character:
    def __init__(self, name, life, weapon=None):
        self.name = name
        self.life = life

    def takeDamage(self):
        damageDone = randint(0, 5)
        self.life -= damageDone
        print(f"The troll attacked! You lost {damageDone} health points.\n")


class Troll(Character):
    def takeDamage(self):
        damageDone = randint(1, 7)
        self.life -= damageDone
        print(f"\nYou damaged the troll! It lost {damageDone} health points.")


def optionScreen():
    print(
        f"You have {goodGuy.life} health points. The troll has {troll.life} health points.")
    choice = input("""
    Choose from the following options:
    1. Fight the troll
    2. Do nothing
    3. Run away\n
    """)
    if choice == "1":
        troll.takeDamage()
        goodGuy.takeDamage()
    elif choice == "2":
        goodGuy.takeDamage()
    elif choice == "3":
        print("COWARD! Better luck next time...")
        exit(0)
    else:
        print("\nPlease enter a valid choice.")
        return optionScreen()


def welcomeMessage():
    print("Welcome to the dungeon! Prepare yourself to battle the troll!")
    goodGuyName = input("What is your name, warrior? ")
    goodGuy = Character(goodGuyName, dice_roll())
    print(f"Good luck, {goodGuyName}.\n")
    return goodGuy


goodGuy = welcomeMessage()
troll = Troll("Troll", 20)
optionScreen()

while goodGuy.life > 0 and troll.life > 0:
    optionScreen()

if goodGuy.life <= 0:
    print("You died. RIP")
else:
    print("You defeated the troll! Amazing!")
