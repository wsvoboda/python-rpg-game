# message to users when opening game
from sys import exit

class Character:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def battleMessage(self):
        print(f"{self.name} has {self.life} health points.")

    def optionScreen(self):
        choice = input("""
        Choose from the following options:
        1. Fight the troll
        2. Do nothing
        3. Run away
        """)
        if choice == "1":
            pass # return goodGuy.attack() - function from Jorge  
        elif choice == "2":
            pass # return goodGuy.takedamage() - function from Jorge
        elif choice == "3": 
            print("COWARD!") 
            exit(0)
        else:
            print("Please enter a valid choice.")
            return self.optionScreen

    def attack(self):
        pass
    
    def takeDamage(self):
        pass
        
    
goodGuy = Character(goodGuyName, 20)
troll = Character("Troll", 20)

print("Welcome to the dungeon! Prepare yourself to battle the troll!")
goodGuyName = input("What is your name, warrior? ")
print(f"Good luck, {goodGuyName}.\n")

while goodGuy.life > 0 and troll.life > 0:
    battleMessage()

if goodGuy.life <= 0:
    print("You died. RIP")
else:
    print("You defeated the troll! Amazing!")


