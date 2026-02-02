#MW_CP2 dice closure fuction:

from helper import u_input, choice_input, int_input

import random

#function for creating new die
def die(sides):
    def amountRolled(ammount):
        dice = []
        for i in range(ammount):
            dice.append(random.randint(1, sides))

        return dice
    
    return amountRolled

#dice rolling function
def rolling():
    #create all functions
    d4 = die(4)
    d6 = die(6)
    d8 = die(8)
    d10 = die(10)
    percentile = die(100)
    d12 = die(12)
    d20 = die(20)

    #roll dice
    def rolled(die):
        
        #show rolled dice
        def showing(already_rolled):
            counter = 0
            for i in already_rolled:
                counter += 1
                print(f"Die {counter}: {i}")

            print(f"Sum: {sum(already_rolled)}")


        #ask for how many dice to roll
        sides = int_input(1000000000000, "How many dice are you rolling?\n> ")
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


    #ask what dice to roll
    die_pick = choice_input(['1','2','3','4','5','6','7'], f"What die would you like to roll? \n1. D4\n2. D6\n3. D8\n4. D10\n5. Percentile (1-100)\n6. D12\n7. D20\n> ")

    rolled(die_pick)


    
    