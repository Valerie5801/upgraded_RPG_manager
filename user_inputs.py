#VY 2nd User Inputs
from helper import choice_input
from helper import u_input
from helper import int_input

#Placeholder list for the conditionals to work. Edit this or any of the input and variables involved in order to make it work with the rest of the code if needed.
exist_inventory = ["potion", "sword", "shield"]

#Inputs for Inventory.
def input_inventory(inventory):
    while True:
        if inventory:
            print("\nHere's the items in your character's inventory:")
            for item in inventory:
                print(item)
        else:
            print("This character has no items in their inventory.")

        add_rem_choice = choice_input(["add", "remove", "done"], '\nDo you want to add or remove an item from their inventory? (add/remove/done)\n> ')
        match add_rem_choice:
            case "add":
                if len(inventory) >= 10:
                    print("Sorry, the inventory is full.")
                else:
                    add_item = u_input("Type the item you want to add to this inventory: ")
                    print(f"{add_item.capitalize()} successfully added to inventory.\n")
                    inventory.append(add_item)
            case "remove":
                if not inventory:
                    print('No item to remove!')
                    continue
                remove_item = choice_input(inventory, "Type the item you want to remove from this inventory: ")
                print(f"{remove_item.capitalize()} successfully removed from inventory.\n")
                inventory.remove(remove_item)
            case "done":
                break
    return inventory


#Inputs for Character Creation. I don't know if this needs parameters.
def input_create_char():
    new_name = input("Name for the new character?: ")
    #Print the available races here
    new_race = input("What race do you want?: ")

    user_stat_choice = choice_input(["set", "generate"], "Do you want to set your own stats or generate random ones?(set/generate): ")
    match user_stat_choice:
        case "set":
            print("Setting stat values...")
            #put the proper thing where it lets the user set stats.
        case "generate":
            print("Values have been generated.")
            #put the thing where we can generate values here

    print(f"Setting Inventory for {new_name}")
    while True:
        new_item = u_input('Type the item you want to add to this inventory(Type "done" to exit): ')
        if new_item.strip().lower() == "done":
            print("Done with the inventory.")
            break
        else:
            print(f"{new_item.capitalize()} added to inventory.")
        
    #break out of the while true loop once user says they're done
    print(f"Type the level of {new_name}:")
    new_char_lvl = int_input()
