#VY 2nd Menu
from helper import u_input, choice_input
from character_search import search
from user_inputs import input_inventory
from character_create import character_create
from skill_management import level_up, skill_allocation, skill_reset
example_learned_skills = set()
character_index = {'example': {
    "key info" : ('orc','wizard'), #race and class

    "stats" : {'strength': 11,'dexterity': 11,'resilience': 11,'magic': 11},

    "skills" : {'attack magic': 0,'buff magic': 0},

    "learned skills" : example_learned_skills,

    "inventory" : [],

    "level": 1,

    "skill points": 3
}}
def main_menu():
    def get_character():
        if not character_index:
            print("You must make a character first!")
            character_create(character_index)
        character = search(character_index)
        return character_index[character]
    while True:
        print("\nYou can: \n1. Create a Character \n2. Edit a Character \n3. View a Character \n4. Exit the Program(This will wipe all data!)")
        user_choice = choice_input(['1','2','3','4'],"Type the number that corresponds with the action that you want to perform: ")
        print("")
        match user_choice:
            case "1":
                character_create(character_index)
            case "2":
                character = get_character()
                print('1. Edit Inventory\n2. Level Up\n3. Allocate Skill Points\n4. Reset Skill Points')
                edit_choice = choice_input(['1','2','3','4'])
                match edit_choice:
                    case "1":
                        character['inventory'] = input_inventory(character['inventory'])
                    case "2":
                        character = level_up(character)
                    case "3":
                        character = skill_allocation(character)
                    case "4":
                        character = skill_reset(character)
                        character = skill_allocation(character)
                    case _:
                        print("An error ocurred. Please try again.")
            case "3":
                character = get_character()
                print(f'Race: {character['key info'][0]}\n')
                print(f'Class: {character['key info'][1]}\n')
                print('Stats:')
                for stat in character['stats']:
                    print(f'{stat}: {character['stats'][stat]}')
                print('\nSkills:')
                for skill in character['skills']:
                    print(f'{skill}: {character['skills'][skill]}')
                print('\nInventory:')
                for item in character['inventory']:
                    print(item)
                print(f'\nLevel: {character['level']}')
                print(f'\nSkill Points: {character['skill points']}')

            case "4":
                break
            case _:
                print("That isn't an option, please try again.")

print("This is an RPG Character Manager.")
main_menu()
print("Thank you for using the Character Manager.")