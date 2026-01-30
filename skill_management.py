from level_info import class_info
from helper import choice_input, int_input
def level_up(character):
    char_class = character['key info'][1]
    character['level'] += 1
    char_lvl = character['level']
    lvl = class_info(char_class,char_lvl)
    character['skill points'] += lvl['skill points']
    for skill in lvl['skills']:
        if not skill in character['learned skills']:
            character['skills'][skill] = 0
            character['learned skills'].add(skill)
    for i in range(lvl['abilities']):
        print('What ability do you want to increase? (strength, dexterity, resilience, magic)')
        choice = choice_input(['stength','dexterity','resilience','magic'])
        character['stats'][choice] += 1
    if character['skill points'] > 0:
        character = skill_allocation(character)
    return character

def skill_allocation(character):
    while character['skill points'] > 0:
        print(f'\nYou have {character['skill points']} skill points to spend.')
        print('Assign skill point where?: ')
        for i in character['skills'].keys():
            print(f'\t{i.capitalize()}: {character['skills'][i]}')
        chosen_skill = choice_input(character['skills'].keys())
        put_in = int_input(character['skill points'], 'How many skill points would you like to input? ', 0)
        character['skills'][chosen_skill] += put_in
        print(f'Added {put_in} skill point to {chosen_skill}.\n')
        character['skill points'] -= put_in
    return character

def skill_reset(character):
    skills = character['skills']
    for i in skills.keys():
        character['skill points'] += skills[i]
        character['skills'][i] = 0
    return character