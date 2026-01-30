#MW_CP2 dice closure fuction:

from helper import u_input, choice_input, int_input

import random

def die(sides):
    def amountRolled(ammount):
        dice = []
        for i in range(ammount):
            dice.append(random.randint(1, sides))

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


    def rolled(die):

        def showing(already_rolled):
            for i in already_rolled:
                print(f"one die rolled a {i}")

            print(f"all dice added together is {sum(already_rolled)}")



        sides = int_input(1000000000000, "how many dice are you rolling?\n Input here:")
        if die == '1':
            showing(d4(sides))
        elif die == '2':
            showing(d6(sides))
        elif die == '3':
            showing(d8(sides))
        elif die == '4':
            showing(d10(sides))
        elif die == '5':
            showing(percentile(sides))
        elif die == '6':
            showing(d12(sides))
        elif die == '7':
            showing(d20(sides))



    die_pick = choice_input(['1','2','3','4','5','6','7'], f"Press 1 if you would like to roll a D4 (die with four sides)\nPress 2 if you would like to use a D6 (die with 6 sides)\nPress 3 if you would like to use a D8 (die with 8 sides)\nPress 4 to use a D10 (die with 10 sides)\nPress 5 to use the Percentile die (die with 100 sides)\nPress 6 for the D12 (die with 12 sides)\nPress 7 for a D20 (die with 20 sides)\n Input here: ")

    rolled(die_pick)

rolling()
    
    