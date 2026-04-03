#AS 2nd character creation for RPG character manager
import random
from helper import u_input, choice_input, int_input
from user_inputs import input_inventory
from skill_management import level_up
from char_classes import Character
#data
character_index = {}
races = ['human', 'orc', 'elf', 'dwarf']
classes = ['cleric', 'wizard', 'fighter', 'rogue']
racial_bonuses = {
    'human': {
        'strength': 1,
        'dexterity': 1,
        'resilience': 1,
        'magic': 1,
        'skills': set()
    },
    'orc': {
        'strength': 2,
        'dexterity': 0,
        'resilience': 1,
        'magic': 0,
        'skills': {'physical attack'}
    },
    'elf': {
        'strength': 0,
        'dexterity': 2,
        'resilience': 0,
        'magic': 1,
        'skills': {'buff magic'}
    },
    'dwarf': {
        'strength': 1,
        'dexterity': 0,
        'resilience': 2,
        'magic': 0,
        'skills': {'defense boost'}
    }
}

#character creation
#edited to work with the Character class
def character_create(character_index):
    #stat generation
    def stat_gen():

        #generate stats
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
        
    
        
    #get character name
    while 14:
        name = u_input("What is your character's name?: ")
        if not name in character_index.keys():
            character_index[name] = {}
            break
        else:
            print("You already have a character with that name. Please try again.")
            continue
    
    #get character race
    print(f"Here are the available races: {', '.join(races)}")
    race_input = choice_input(races,f"What is {name.capitalize()}'s race?: ")

    #get character class
    print(f"Here are the available classes: {', '.join(classes)}")
    class_choice = choice_input(classes,f"What is {name.capitalize()}'s class?: ")


    #ask user if they want to make a backstory about their character.
    ask_backstory = choice_input(["yes", "no"], f"Do you want to add a backstory for {name.capitalize()}?: ")
    if ask_backstory == "yes":
        print(f"Type {name.capitalize()}'s backstory and press ENTER when done.")
        char_back = input("> ")
    else:
        char_back = ""

    #create character object using Character class
    """character_index[name]['key info'] = (raceinput,class_choice)
    character_index[name]['skills'] = {}
    character_index[name]['level'] = 0
    character_index[name]['skill points'] = 0
    character_index[name]['learned skills'] = set()"""
    new_char = Character(name.capitalize(), race_input, class_choice, char_back)

    #get initial inventory. edited to work with the Character class
    print(f"\nSetting {new_char.name}'s inventory...")
    """character_index[name]['inventory'] = input_inventory([])
    character_index[name]['stats'] = {}"""
    input_inventory(new_char)

    #get initial stats
    print(f"\nSetting {new_char.name}'s stats...")
    print("You can: \n1. Use generated stats \n2. Set your own stats")
    uinput = choice_input(['1', '2'], "What do you want to do?(1/2): ")
    match uinput:
        case '1': #generate stats
            stat_list = stat_gen()
            print('Generated Stats!')
            for i in stat_list: print(i)
        case '2': #get stat inputs (max 20)
            stat_list = []
            for i in range(4):
                stat_list.append(int_input(20,f'stat {i+1}: '))
    
    #ask where to assign stat values. moved this code over to the class and made it a method.
    """remaining = {'strength','dexterity','magic','resilience'}
    for stat in stat_list:
        display_remaining = ', '.join([i.title() for i in remaining])
        if len(remaining) > 1:
            print(f'What stat do you want the value {stat} to be? ({display_remaining})')
            to_place = choice_input(remaining)
        else:
            print(f'Assigned {stat} to {display_remaining}')
            to_place = list(remaining)[0]
        character_index[name]['stats'][to_place] = stat
        remaining.remove(to_place)"""
    new_char.set_init_skills(stat_list)

    #add racial stat bonuses
    """for i in character_index[name]['stats'].keys():
        character_index[name]['stats'][i] += racial_bonuses[race_input][i]"""

    #add racial learned skills
    """for skill in racial_bonuses[race_input]['skills']:
        if not skill in character_index[name]['learned skills']:
            character_index[name]['learned skills'].add(skill)
            character_index[name]['skills'][skill] = 0
        character_index[name]['skills'][skill] += 1"""

    #display final stats
    print('\nHere are your final stats:')
    """for stat in character_index[name]['stats']:
        print(f'{stat}: {character_index[name]['stats'][stat]}')
    character_index[name] = level_up(character_index[name])
    print(f'{name.capitalize()} has been created!')"""
    print(new_char)
    return new_char

demo = {'example': {
    "key info" : ('orc','wizard'), #race and class

    "stats" : {'strength': 11,'dexterity': 11,'resilience': 11,'magic': 11},

    "skills" : {'attack magic': 0,'buff magic': 0},

    "learned skills" : set(),

    "inventory" : [],

    "level": 1,

    "skill points": 3
}}

character_create(demo)