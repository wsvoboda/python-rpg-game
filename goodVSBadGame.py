from random import randint # to be able to generate a random number for the attack

class Character: 
    def __init__(self, name, defense, power, life):
        self.name = name
        self.defense = defense
        self.power = power
        self.life = life

    def takeDamage(self):
        damageDone = randint(0,5) - (self.defense//10)
        if damageDone <= 0:
            print(f"The troll's attack missed! You didn't lose any health points.")
        else:
            self.life -= damageDone
            print(f"The troll attacked! You lost {damageDone} health points.\n")

class Troll(Character):
    def takeDamage(self):
        damageDone = randint(0,7) + ((goodGuy.power)//10)
        if damageDone <= 0:
            print(f"Your attacked missed! The troll didn't lost any health points.")
        else:
            self.life -= damageDone
            print(f"\nYou attacked the troll! It lost {damageDone} health points.")

def optionScreen():
    print(f"""
    {goodGuy.name}: {goodGuy.life} health points
    Troll: {troll.life} health points
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
    goodGuy = Character(goodGuyName, 0, 0, 20)
    print(f"Good luck, {goodGuyName}.\n")
    return goodGuy

goodGuy = welcomeMessage()
troll = Troll("Troll", 0, 0, 20)
optionScreen()

while goodGuy.life > 0 and troll.life > 0:
    optionScreen()

if goodGuy.life <= 0:
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



