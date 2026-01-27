#MW_CP2 dictionary of characters

import random

characters = {
    "base" : {
        "class" : "",

        "race" : "",

        "stats" : (0,0,0,0),#strength, dexterity, ressilience, and magic

        "skills" : {},

        "inventory" : []
    }
}

races = {
    "human" : (1,1,1,1),

    "dwarf" : (1,0,2,1),

    "elf" : (0,2,0,2),

    "orc" : (2,-1,3,0)
}

def roll():
    dice = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]

    dice.remove(min(dice))

    stat = sum(dice)
    return stat

def statAddition(race, char_choice, chars):
    indexing = 0
    while indexing > 4:
        
        


def statDecision(char_choice, chars):
    while True:
        race = input("What race would you like? Human, Dwarf, Elf, or Orc?").strip().lower()

        match race:
            case "human":
                pass
                break

            case "dwarf":
                pass
                break

            case "elf":
                pass
                break

            case "orc":
                pass
                break

            case _:
                pass
