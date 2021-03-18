# message to users when opening game

class Character:
    def __init__(self, name, life):
        self.name = name
        self.life = life

def openingMessage():
    print("Welcome to the dungeon! Prepare yourself to battle the troll!")
    goodGuyName = input("What is your name, warrior? ")
    print(f"Good luck, {goodGuyName}.\n")

def battleMessage():
    print("You have 10 health points. The troll has 10 health points.")
    print("""
    Choose from the following options:
    1. Fight the troll
    2. Do nothing
    3. Run away
    """)

openingMessage()
battleMessage()