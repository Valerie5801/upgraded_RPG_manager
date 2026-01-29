#MW_CP2 dice closure fuction:

from helper import u_input, choice_input, int_input

import random

def die(sides):
    def amountRolled(ammount):
        dice = {

        }
        for i in range(ammount):
            dice[i] = random.randint(1, sides)

        return dice
    
    return amountRolled

def rolling():
    d4 = die(4)
    d6 = die(6)
    d8 = die(8)
    d10 = die(10)
    percentile = die(100)
    d12 = die(12)
    d20 = die(20)
    choice_input(['1','2','3','4','5','6','7'])

    