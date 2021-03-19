from random import randint

class Character:
    def __init__(self, name, lifePoints):
        self.name = name
        self.lifePoints = lifePoints
    
    def takeDamage(self):
        damageDone = randint(0,5)
        self.lifePoints -= damageDone
        print(f"The {badGuyName} attacked! You lost {damageDone} health points.\n")

class EvilCharacter(Character):
    
    def takeDamage(self):
        damageDone = randint(1,7)
        self.lifePoints -= damageDone
        print(f"\nYou damaged the {badGuyName}! It lost {damageDone} health points.")

# badGuyName = random(troll, goblin, bigFoot)
troll = EvilCharacter("Troll", 20)
goblin = EvilCharacter("Goblin", 20)
bigFoot = EvilCharacter("Big Foot", 30)

# badGuyName = ("Troll", "Goblin", "Big Foot")
# badGuy = EvilCharacter(badGuyName, 20)


def optionScreen():
    print(f"You have {goodGuy.lifePoints} health points. The {badGuyName} has {badGuy.lifePoints} health points.")
    choice = input("""
    Choose from the following options:
    1. Fight the {badGuyName}
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
    print("""
    .:\:\:/:/:.
   :.:\:\:/:/:.:
  :=.' -   - '.=:
   '=(\ 9   9 /)='
     (  (_)  )
     /`-vvv-'|
    /         |
   / /|,,,,,|\ |
  /_//  /^\  \\_|
  WW(  (   )  )WW
   __\,,\ /,,/__
  (______Y______)
        
Welcome to the dungeon! Prepare yourself to battle!""")
    goodGuyName = input("What is your name, warrior? ")
    goodGuy = Character(goodGuyName, 20)
    print(f"Good luck, {goodGuyName}.\n")
    return goodGuy

goodGuy = welcomeMessage()
optionScreen()

while goodGuy.lifePoints > 0 and troll.lifePoints > 0:
    optionScreen()

if goodGuy.lifePoints <= 0:
    print("You died. RIP")
else:
    print("You defeated the {badGuyName}. Amazing!")