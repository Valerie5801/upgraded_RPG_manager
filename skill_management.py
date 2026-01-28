from level_info import class_info
from helper import choice_input
def level_up(character):
    char_class = character['class']
    character['lvl'] += 1
    char_lvl = character['lvl']
    lvl = class_info(char_class,char_lvl)
    character['skill points'] += lvl['skill points']
    for skill in lvl['skills']:
        if not skill in character['learned skills']:
            character['skills'][skill] = 0
            character['learned skills'].append(skill)
    for i in range(lvl['abilities']):
        print('What ability do you want to increase? (strength, dexterity, resilience, magic)')
        choice = choice_input(['strength','dexterity','resilience','magic'])
        character['stats'][choice] += 1
    return character
def skill_allocation(character):
    for i in range(character['skill points']):
        print(f'You have {character['skill points']} skill points to spend.')
        print('Assign skill point where?')
        for i in character['skills'].keys():
            print(f'{i}: {character['skills'][i]}')
        chosen_skill = choice_input(character['skills'].keys())
        character['skills'][chosen_skill] += 1
        print(f'Added one skill point to {chosen_skill}.')
        character['skill points'] -= 1
        return character
def skill_reset(character):
    skills = character['skills']
    for i in skills.keys():
        character['skills'][i] = 0
        character['skill points'] += skills[i]
    return character