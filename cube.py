import random

def  cube_roll():
    return random.randrange(1, 6)
def roll_two_rounds():
    return {p1:cube_roll(), p2:cube_roll()} 