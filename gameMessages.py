from goodVSBadGame import *

def battleOptionScreen():
    print(f"""
    {goodGuy.name}: {goodGuy.lifePoints} health points
    Troll: {troll.lifePoints} health points
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
    goodGuy = Character(goodGuyName, 10, 10, 20)
    print(f"Good luck, {goodGuyName}.\n")
    return goodGuy