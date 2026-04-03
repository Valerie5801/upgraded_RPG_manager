#VY 2nd User Inputs
from helper import choice_input
from helper import u_input

#Placeholder list for the conditionals to work. Edit this or any of the input and variables involved in order to make it work with the rest of the code if needed.
exist_inventory = ["potion", "sword", "shield"]

#Inputs for Inventory
#edit this to work with the Character class
def input_inventory(character):
    #forever
    while True:
        #display inventory
        if character.inventory:
            print("\nHere's the items in your character's inventory:")
            for item in character.inventory:
                print(item)
        else:
            print("This character has no items in their inventory.")

        #get choice on what to do
        add_rem_choice = choice_input(["add", "remove", "done"], '\nDo you want to add or remove an item from their inventory? (add/remove/done)\n> ')
        match add_rem_choice:
            case "add": #add to inventory
                if len(character.inventory) >= 10:
                    print("Sorry, the inventory is full.")
                else:
                    add_item = u_input("Type the item you want to add to this inventory: ")
                    print(f"{add_item.capitalize()} successfully added to inventory.\n")
                    character.inventory.append(add_item)
            case "remove": #remove from inventory
                if not character.inventory:
                    print(f"There is no item to remove in {character.name}'s inventory!")
                    continue
                remove_item = choice_input(character.inventory, "Type the item you want to remove from this inventory: ")
                character.remove_inventory(remove_item)
            case "done": #exit inventory management
                break
    return character
