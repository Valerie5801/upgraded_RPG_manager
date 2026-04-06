#VY 2nd Menu

#Import all functions
from helper import u_input, choice_input
from csv_funcs import rewrite_csv, save_csv
from character_search import search
from user_inputs import input_inventory
from character_create import character_create
from skill_management import level_up, skill_allocation, skill_reset
from dice import rolling
from classes import Character, ExistCharacters, DataVizualization, StatisticalAnalyzer


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
        analytics = StatisticalAnalyzer(characters)
        #get user choice on what to do
        print("\nYou can: \n1. Create a Character \n2. Edit a Character \n3. View a Character \n4. Remove a Character\n5. Compare two Characters\n6. View all characters\n7. Roll some dice\n8. Exit the Program")
        user_choice = choice_input(['1','2','3','4','5','6','7','8'],"Type the number that corresponds with the action that you want to perform: ")
        print("")
        match user_choice:
            #character creation
            case "1":
                new_char = character_create(characters.chars)
                characters.add_char(new_char)
            #character editing
            case "2":
                character = get_character() #get character choice
                print('You can: \n1. Edit Inventory\n2. Level Up\n3. Reset Skill Points\nChange the name/backstory')
                edit_choice = choice_input(['1','2','3','4'], "What would you like to do? (1/2/3/4): ")
                match edit_choice:
                    case "1": #inventory management
                        character = input_inventory(character)
                    case "2": #level up
                        character = level_up(character)
                    case "3": #skill reset
                        character = skill_reset(character)
                        character = skill_allocation(character)
                    case "4":
                        print('Type in "exit" if you want to back out.')
                        choose_change = choice_input(['name', 'backstory', 'both', 'exit'], "What would you like to change?(name/backstory/both/exit): ")
                        old_name = character.name
                        #preserve original values in case they don't change
                        new_name = character.name
                        new_backstory = character.backstory
                        #ask for the values depending on what the user picked
                        match choose_change:
                            case 'name':
                                new_name = u_input(f"What will be {character.name}'s new name?: ")
                            case 'backstory':
                                new_backstory = input(f"Type in the backstory for {character.name} and press ENTER when done: ")
                            case 'both':
                                new_name = u_input(f"What will be {character.name}'s new name?: ")
                                new_backstory = input(f"Type in the backstory for {character.name} and press ENTER when done: ")
                            case 'exit':
                                continue
                        character.edit_info(new_name, new_backstory)

                        #since names are dictionary keys as well, if the name was change, change the key too.
                        if new_name != old_name:
                            characters.chars[new_name] = characters.chars[old_name]
                            del characters.chars[old_name]
                            
                    case _:
                        print("An error ocurred. Please try again.")

            #character viewing
            case "3":
                character = get_character()
                print(character)
                ask_view_graph = choice_input(["yes", "no"], "Do you want to see this character's stats on a graph?: ")
                match ask_view_graph:
                    case "yes":
                        graph = DataVizualization(analytics.df)
                        ask_type_graph = choice_input(["radar", "bar"], "Do you want a bar or radar graph?: ")
                        match ask_type_graph:
                            case "radar":
                                graph.radar_chart(character.name)
                            case "bar":
                                graph.bar_stat(character.name)
                    case "no":
                        continue
            
            #character removal
            case "4":
                character = get_character()
                characters.remove_char(character.name)
                print(f"{character.name} has been removed.")

            #character comparison
            case "5":
                graph = DataVizualization(analytics.df)
                print("Select the first character for comparison.")
                first_char = get_character()
                print("Select the second character for comparison.")
                second_char = get_character()

                selected_chars = [first_char.name, second_char.name]
                print("Type in either strength, dexterity, resilience, or magic. \nAlso note that in the terminal will still be information about the rest of the stats.")
                chosen_stat = choice_input(['strength', 'dexterity', 'resilience', 'magic'], "What stat do you want to compare on the graph?: ")

                graph.compare_stat(chosen_stat, selected_chars)
                comparison_info = analytics.compare_chars(first_char.name, second_char.name)
                for line in comparison_info:
                    print(line)
                    
            #show all characters
            case "6":
                characters.show_chars()

            #dice rolling
            case "7":
                rolling()
            
            #exiting
            case "8":
                break

            #error handling
            case _:
                print("That isn't an option, please try again.")
        
        rewrite_csv(characters.chars)

        #clear screen
        input('Press ENTER to continue > ')
        print("\033c", end="")