from random import randint


def goodGuyRoll():
    input("Press enter to roll the magic dice. ")
    d1 = randint(1, 6)
    print(f"\nYou rolled a {d1}.")
    print(f"You get {d1*10} health points.")
    return d1 * 10

def trollRoll():
    d1 = randint(1, 6)
    print(f"\nThe troll has his own magic dice! It rolled a {d1}.")
    input(f"The troll gets {d1*10} health points.\nPress enter to battle! ")
    return d1 * 10