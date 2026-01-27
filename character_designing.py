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

    "inventory" : []
}

character_index = {
      
}

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
        
        stat_options = {"1" : roll(), "2" : roll(), "3" : roll(), "4" : roll()}
        return [stat_options]

def statBlock(character, character_indx):
    options = statGen
    choices = options.keys
    def playerDecision(stat):
        while True:
            print(f"What would you like your {stat} to be?")
            turns = 0
            while turns < len(choices):
                print(f"Press {choices[turns]} to set strength to {options[choices[turns]]}\n")
                turns += 1
            
            player_choice = input("What is your choice? ")
            if player_choice.isDigit():

        

