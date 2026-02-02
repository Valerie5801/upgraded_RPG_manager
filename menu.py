#VY 2nd Menu

#Import all functions
from helper import u_input, choice_input
from character_search import search
from user_inputs import input_inventory
from character_create import character_create
from skill_management import level_up, skill_allocation, skill_reset
from dice import rolling



#create example character and character index
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
#main menu function
def main_menu():
    #get character function
    def get_character():
        #check if there is a character. If so, search characters. Else, tell them to make a character
        if not character_index:
            print("You must make a character first!")
            character_create(character_index)
        character = search(character_index)
        return character_index[character]
    #loop forever
    while True:
        #get user choice on what to do
        print("\nYou can: \n1. Create a Character \n2. Edit a Character \n3. View a Character \n4. Roll some dice\n5. Exit the Program(This will wipe all data!)")
        user_choice = choice_input(['1','2','3','4','5'],"Type the number that corresponds with the action that you want to perform: ")
        print("")
        match user_choice:
            #character creation
            case "1":
                character_create(character_index)
            
            #character editing
            case "2":
                character = get_character() #get character choice
                print('You can: \n1. Edit Inventory\n2. Level Up\n3. Reset Skill Points')
                edit_choice = choice_input(['1','2','3'], "What would you like to do? (1/2/3): ")
                match edit_choice:
                    case "1": #inventory management
                        character['inventory'] = input_inventory(character['inventory'])
                    case "2": #level up
                        character = level_up(character)
                    case "3": #skill reset
                        character = skill_reset(character)
                        character = skill_allocation(character)
                    case _:
                        print("An error ocurred. Please try again.")

            #character viewing
            case "3":
                character = get_character()
                print(f'\nRace: {character['key info'][0]}') #race
                print(f'Class: {character['key info'][1]}') #class
                print('\nStats:')
                for stat in character['stats']:
                    print(f'{stat}: {character['stats'][stat]}') #stat
                print('\nSkills:')
                for skill in character['skills']:
                    print(f'{skill}: {character['skills'][skill]}') #skill
                print('\nInventory:')
                for item in character['inventory']:
                    print(item) #inventory item
                print(f'Level: {character['level']}') #level
                print(f'Skill Points: {character['skill points']}') #unspent skill points
            
            #dice rolling
            case "4":
                rolling()
            
            #exiting
            case '5':
                break

            #error handling
            case _:
                print("That isn't an option, please try again.")
        
        #clear screen
        input('Press ENTER to continue > ')
        print("\033c", end="")

#run main function
print("This is an RPG Character Manager.")
main_menu()
print("Thank you for using the Character Manager.")