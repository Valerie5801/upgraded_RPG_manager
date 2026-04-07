from level_info import class_info
from helper import choice_input, int_input

#level up function
def level_up(character):
    #get character class
    char_class = character.role
    if character.level < 10:
        #increase character level
        character.level += 1
        #retrieve level info
        char_lvl = character.level
        lvl = class_info(char_class,char_lvl)
        #add skill points
        character.skill_points += lvl['skill points']
        #add new learned skills
        for skill in lvl['skills']:
            if not skill in character.skills:
                character.skills[skill] = 0
        #add ability increases
        for i in range(lvl['abilities']):
            print('What ability do you want to increase? (strength, dexterity, resilience, magic)')
            choice = choice_input(['strength','dexterity','resilience','magic'])
            character.stats[choice] += 1
        #run skill allocation
        if character.skill_points > 0:
            character = skill_allocation(character)
    else:
        print(f"{character.name} is already level 10.")
    return character

#skill allocation
def skill_allocation(character):
    #if the character has no skills yet, tell the user.
    if not character.skills:
        print("No skills are available to assign skill points to right now.")
        print("Earn a skill first by leveling up or choosing a race/class that grants a starting skill.")
        return character

    #run until character has no skill points
    while character.skill_points > 0:
        print(f'\nYou have {character.skill_points} skill points to spend.')
        #get input on where to assign skill points
        print('Assign skill point where?: ')
        for i in character.skills.keys():
            print(f'\t{i.capitalize()}: {character.skills[i]}')
        chosen_skill = choice_input(character.skills.keys())
        #ask how many skill points to assign
        put_in = int_input(character.skill_points, 'How many skill points would you like to input? ', 0)
        #increase skills
        character.skills[chosen_skill] += put_in
        print(f'Added {put_in} skill point to {chosen_skill}.\n')
        #reduce unspent skill points
        character.skill_points -= put_in
    return character

#skill reset
def skill_reset(character):
    #reset skills and add those skill points to unspent
    skills = character.skills
    for i in skills.keys():
        character.skill_points += skills[i]
        character.skills[i] = 0
    return character