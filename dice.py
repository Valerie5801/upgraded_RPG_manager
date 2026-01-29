#MW_CP2 dice closure fuction:

import random

def die(sides):
    def amountRolled(ammount):
        dice = {

        }
        for i in range(ammount):
            dice[i] = random.randint(1, sides)

        return dice
    
    return amountRolled

percentile = die(100)
value = percentile(3)
for i in value:
    print(f"die {i+1} is {value[i]}")

    