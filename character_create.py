#AS 2nd character creation for RPG character manager
import random
from helper import u_input
character_index = {}

def character_create(character_index):

    def stat_gen():

        def roll():
            dice = [random.randint(1,6), random.randint(1,6), random.randint(1,6),random.randint(1,6)]
            dice.remove(min(dice))
            stat = sum(dice)
            return stat
        
        return [roll(), roll(), roll(), roll()]
    
    def check(input, character_index):
        if input in character_index:
            return True
        else:
            return False
    
    while 14:
        name = u_input("What is your character's name? ").title()
        if check(name, character_index) == False:
            character_index[name] = {}
            break
        else:
            print("You already have a character with that name. Please try again.")
            continue
    
    character_index[name['Race']] = u_input('What is your race? ').title()

    