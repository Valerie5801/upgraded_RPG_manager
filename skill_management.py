from level_info import class_info
from helper import choice_input
def level_up(character):
    char_class = character['class']
    character['lvl'] += 1
    char_lvl = character['lvl']
    lvl = class_info(char_class,char_lvl)
    character['skill points'] += lvl['skill points']
    for skill in lvl['skills']:
        if not skill in character['skills'].keys():
            character['skills'][skill] = 0
    for i in range(lvl['abilities']):
        print('What ability do you want to increase? (strength, dexterity, resilience, magic)')
        choice = choice_input(['strength','dexterity','resilience','magic'])
        character['stats'][choice] += 1
    return character
def skill_allocation(character):
    for i in range(character['skill points']):
        print('Assign skill points where?')
        for i in character['skills'].keys():
            print(f'{i}: {character['skills'][i]}')
            #NOT FINISHED! DON'T USE THIS