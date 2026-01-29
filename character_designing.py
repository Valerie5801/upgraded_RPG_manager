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
        choice = input(f"Press 1 if you would like your strength to be{stats_to_be_used[0]}\nPress 2 if you would like your strength to be{stats_to_be_used[1]}\nPress 3 if you would like your strength to be{stats_to_be_used[2]}\nPress 4 if you would like your strength to be{stats_to_be_used[3]}\n")
        match choice:
            case "1":
                strength = stats_to_be_used[0]
                stats_to_be_used.remove(stats_to_be_used[0])
                break
            case "2":
                strength = stats_to_be_used[1]
                stats_to_be_used.remove(stats_to_be_used[1])
                break
            case "3":
                strength = stats_to_be_used[2]
                stats_to_be_used.remove(stats_to_be_used[2])
                break
            case "4":
                strength = stats_to_be_used[3]
                stats_to_be_used.remove(stats_to_be_used[3])
                break
            case _:
                pass

    while True:
        print("\n\nYou are currently picking for dexterity\n")
        choice = input(f"Press 1 if you would like your strength to be{stats_to_be_used[0]}\nPress 2 if you would like your strength to be{stats_to_be_used[1]}\nPress 3 if you would like your strength to be{stats_to_be_used[2]}\n")
        match choice:
            case "1":
                dexterity = stats_to_be_used[0]
                stats_to_be_used.remove(stats_to_be_used[0])
                break
            case "2":
                dexterity = stats_to_be_used[1]
                stats_to_be_used.remove(stats_to_be_used[1])
                break
            case "3":
                dexterity = stats_to_be_used[2]
                stats_to_be_used.remove(stats_to_be_used[2])
                break
            case _:
                pass

    while True:
        print("\n\nYou are currently picking for ressiliance\n")
        choice = input(f"Press 1 if you would like your strength to be{stats_to_be_used[0]}\nPress 2 if you would like your strength to be{stats_to_be_used[1]}\n")
        match choice:
            case "1":
                ressiliance = stats_to_be_used[0]
                stats_to_be_used.remove(stats_to_be_used[0])
                break
            case "2":
                ressiliance = stats_to_be_used[1]
                stats_to_be_used.remove(stats_to_be_used[1])
                break
            case _:
                pass

    print(f"your magic stat is: {stats_to_be_used[0]}")
    magic = stats_to_be_used[0]
    strength += races[character_index[character]['race']][0]
    dexterity += races[character_index[character]['race']][1]
    ressiliance += races[character_index[character]['race']][2]
    magic += races[character_index[character]['race']][3]
    return (strength, dexterity, ressiliance, magic)
        

