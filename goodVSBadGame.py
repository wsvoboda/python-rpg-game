from dice_roll import *
from random import randint

class Character: 
    def __init__(self, name, lifePoints):
        self.name = name
        self.lifePoints = lifePoints

    def takeDamage(self):
        damageDone = randint(0,8)
        if damageDone <= 0:
            print(f"The troll attacked but missed! You didn't lose any health points.")
        else:
            self.lifePoints -= damageDone
            print(f"The troll attacked! You lost {damageDone} health points.\n")

class EvilCharacter(Character):
    def takeDamage(self):
        damageDone = randint(0,10)
        if damageDone <= 0:
            print(f"Your attacked missed! The troll didn't lost any health points.")
        else:
            self.lifePoints -= damageDone
            print(f"\nYou attacked the troll! It lost {damageDone} health points.")
            
trollPicture = """
    .:\:\:/:/:.
   :.:\:\:/:/:.:
  :=.' -   - '.=:
  '=(\ 9   9 /)='
     (  (_)  )
     /`-vvv-'|
    /         |
   / /|,,,,,|\ |
  /_//  /^\  \\\_|
  WW(  (   )  )WW
   __\,,\ /,,/__
  (______Y______)
  """

def battleOptionScreen():
    print(f"""{trollPicture}
    {goodGuy.name}: {"*" * goodGuy.lifePoints} ({goodGuy.lifePoints}) health points
    Troll: {"*" * troll.lifePoints} ({troll.lifePoints}) health points
    """)
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
        print("You stood around and did nothing.. Try harder next time! The troll takes no breaks!")
        goodGuy.takeDamage()
    elif choice == "3":
        print("COWARD! Better luck next time...")
        exit(0)
    else:
        print("\nPlease enter a valid choice.")
        return optionScreen()

def welcomeMessage():
    print("""
            /
    *//////{<>==================-
            \\
    
    Welcome to the dungeon! Prepare yourself to battle the troll!

            /
    *//////{<>==================-
            \\
    """)

    goodGuyName = input("What is your name, warrior? ")
    goodGuy = Character(goodGuyName, goodGuyRoll())
    print(f"Good luck, {goodGuyName}.\n")
    return goodGuy


goodGuy = welcomeMessage()

troll = EvilCharacter("Troll", trollRoll())
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