from random import randint


def dice_roll():
    input("Press enter to roll the magic dice. ")
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(f"You rolled a {d1} and a {d2}")
    print(f"You get this weapon and {d1 *10} points")
    return d1 * 10
