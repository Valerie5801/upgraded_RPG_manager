#AS 2nd character creation for RPG character manager
import random
from helper import u_input, choice_input, int_input
from user_inputs import input_inventory
from skill_management import level_up

character_index = {}
races = ['human', 'orc', 'elf', 'dwarf']
classes = ['cleric', 'wizard', 'fighter', 'rogue']


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
        name = u_input("What is your character's name? ")
        if not name in character_index.keys():
            character_index[name] = {}
            break
        else:
            print("You already have a character with that name. Please try again.")
            continue
    raceinput = choice_input(races,f'What is your race? Races include: {races}. ')
    class_choice = choice_input(classes,f'What is your class? Classes include: {classes}. ')
    character_index[name]['key info'] = (raceinput,class_choice)
    character_index[name]['skills'] = {}
    character_index[name]['level'] = 0
    character_index[name]['skill points'] = 0

    character_index[name]['learned skills'] = set()
    character_index[name]['inventory'] = input_inventory([])
    character_index[name]['stats'] = {}
    uinput = choice_input(['1', '2'], '1: premade stats\n2: make your own\n> ')
    match uinput:
        case '1':
            stat_list = stat_gen()
            print('Generated Stats!')
            for i in stat_list: print(i)
        case '2':
            stat_list = []
            for i in range(4):
                stat_list.append(int_input(20,f'stat {i+1}: '))
    
    remaining = {'strength','dexterity','magic','resilience'}
    for stat in stat_list:
        display_remaining = ', '.join([i.title() for i in remaining])
        print(f'Where would you like your {stat}? ({display_remaining})')
        to_place = choice_input(remaining)
        character_index[name]['stats'][to_place] = stat
        remaining.remove(to_place)
    print('Here are your final stats:')
    for stat in character_index[name]['stats']:
        print(f'{stat}: {character_index[name]['stats'][stat]}')
    character_index[name] = level_up(character_index[name])
    print(f'{name} has been created!')
    return character_index
