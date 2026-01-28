#AS 2nd character creation for RPG character manager
import random
from helper import u_input, choice_input
character_index = {}
races = ['Human', 'Orc', 'Elf', 'Dwarf']
classes = ['Cleric', 'Wizard', 'Fighter', 'Rougue']


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
        
    def stat_creation(character_index, stat_index, name):
        uinput = choice_input(['1', '2'], 'Would you like 1: premade stats, or 2: make your own? ')
        if uinput == '1':
            stat_list = stat_gen()
            for i in stat_index:
                choice_input()
    
    while 14:
        name = u_input("What is your character's name? ").title()
        if check(name, character_index) == False:
            character_index[name] = {}
            break
        else:
            print("You already have a character with that name. Please try again.")
            continue
    
    while 143:
        raceinput = u_input(f'What is your race? Races include: {races}. ').title()
        if check(raceinput, races):
            character_index[name]['Race'] = raceinput
            break
        else:
            print('Invalid choice.')
            continue
    
    while 143:
        character_index[name]['Class'] = u_input(f'What is your class? Classes include: {classes}. ').title()
        if check(character_index[name]['Class'], classes):
            break
        else:
            print('Invalid choice.')
            continue

    
    
    character_index[name]['Skills'] = {}

    return character_index

print(character_create(character_index))
print(character_create(character_index))