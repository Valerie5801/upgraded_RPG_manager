#MW_CP2 dictionary of characters
from helper import u_input
from helper import int_input
from helper import choice_input

import random

character_base = {
    "class" : "",

    "race" : "",

    "stats" : (0,0,0,0),#strength, dexterity, ressilience, and magic

    "skills" : {},

    "learned skills" : {},

    "inventory" : []
}

character_index = {
      
}
#character_index["Samantha"] = character_base
races = {
    "human" : (1,1,1,1),

    "dwarf" : (1,0,2,1),

    "elf" : (0,2,0,2),

    "orc" : (2,-1,3,0)
}

def statGen():

        def roll():
            dice = [random.randint(1,6), random.randint(1,6), random.randint(1,6),random.randint(1,6)]
            dice.remove(min(dice))
            stat = sum(dice)
            return stat
        
        stat_options = [roll(),roll(),roll(),roll()]
        return [stat_options]

def statBlock(character, character_indx):
    stats_to_be_used = statGen()
    while True:
        print("\n\nYou are currently picking for strength\n")
        choice = input(f"Press 1 if you would like your strength to be{stats_to_be_used[0]}\nPress 2 if you would like your strength to be{stats_to_be_used[1]}\nPress 3 if you would like your strength to be{stats_to_be_used[2]}\nPress 4 if you would like your strength to be{stats_to_be_used[3]}")
        if choice

        

