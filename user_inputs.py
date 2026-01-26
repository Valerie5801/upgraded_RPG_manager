#VY 2nd User Inputs
from helper import choice_input
from helper import u_input

#Inputs for Inventory
print("Do you want to add or remove an item?(add/remove): ")
add_rem_choice = choice_input(["add", "remove"])

match add_rem_choice:
    case "add":
        #part to check if inventory is full
        #if it's not
        print("Type the item you want to add to this inventory.")
        add_item = u_input()
        #if it is
        print("Sorry, the inventory is full.")
    case "remove":
        print("Type the item you want to remove from this inventory.")
        remove_item = u_input()
        #Check if the item exists and remove it if it does. if it doesn't, print the following
        print("That item doesn't exist.")



#Inputs for Character Creation
new_name = input("Name for the new character?: ")
#Print the available races
new_race = input("What race do you want?: ")