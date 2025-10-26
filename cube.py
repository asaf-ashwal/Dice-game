import random

def  cube_roll():
    return random.randrange(1, 6)


def roll_two_rounds():
    return  (cube_roll(), cube_roll())
