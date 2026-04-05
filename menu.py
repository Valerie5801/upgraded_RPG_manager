#VY 2nd Menu

#Import all functions
from helper import u_input, choice_input, rewrite_csv, save_csv
from character_search import search
from user_inputs import input_inventory
from character_create import character_create
from skill_management import level_up, skill_allocation, skill_reset
from dice import rolling
from char_classes import Character, ExistCharacters


#create example character and character index
example_learned_skills = set()
"""character_index = {'example': {
    "key info" : ('orc','wizard'), #race and class

    "stats" : {'strength': 11,'dexterity': 11,'resilience': 11,'magic': 11},

    "skills" : {'attack magic': 0,'buff magic': 0},

    "learned skills" : example_learned_skills,

    "inventory" : [],

    "level": 1,

    "skill points": 3
}}"""


character_index = save_csv()
#failsafe incase nothing is in the CSV
if not character_index:
    character_index = {'example': Character('Example', 'orc', 'wizard', 'this is just an example character')}
#main menu function
def main_menu():
    characters = ExistCharacters(character_index)

    #get character function
    def get_character():
        #check if there is a character. If so, search characters. Else, tell them to make a character
        if not characters.chars:
            print("You must make a character first!")
            new_char = character_create(characters.chars)
            characters.add_char(new_char)
        character = search(characters.chars)
        return characters.chars[character]
    #loop forever
    while True:
        #get user choice on what to do
        print("\nYou can: \n1. Create a Character \n2. Edit a Character \n3. View a Character \n4. Remove a Character\n5. Compare two Characters\n6. Roll some dice\n7. Exit the Program")
        user_choice = choice_input(['1','2','3','4','5','6','7'],"Type the number that corresponds with the action that you want to perform: ")
        print("")
        match user_choice:
            #character creation
            case "1":
                new_char = character_create(characters.chars)
                characters.add_char(new_char)
            #character editing
            case "2":
                character = get_character() #get character choice
                print('You can: \n1. Edit Inventory\n2. Level Up\n3. Reset Skill Points')
                edit_choice = choice_input(['1','2','3'], "What would you like to do? (1/2/3): ")
                match edit_choice:
                    case "1": #inventory management
                        character = input_inventory(character)
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
                print(character.name)
            
            #character removal
            case "4":
                character = get_character()
                characters.remove_char(character.name)
                print(f"{character.name} has been removed.")

            #character comparison
            case "5":
                pass

            #dice rolling
            case "6":
                rolling()
            
            #exiting
            case "7":
                break

            #error handling
            case _:
                print("That isn't an option, please try again.")
        
        rewrite_csv(characters.chars)

        #clear screen
        input('Press ENTER to continue > ')
        print("\033c", end="")