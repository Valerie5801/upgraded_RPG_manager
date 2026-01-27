#VY 2nd User Inputs
from helper import choice_input
from helper import u_input
from helper import int_input

#Inputs for Inventory
print("Do you want to add or remove an item?(add/remove): ")
add_rem_choice = choice_input(["add", "remove"], "Do you want to add or remove an item?(add/remove): ")

match add_rem_choice:
    case "add":
        #part to check if inventory is full
        #if it's not
        add_item = u_input("Type the item you want to add to this inventory: ")
        #if it is
        print("Sorry, the inventory is full.")
    case "remove":
        remove_item = u_input("Type the item you want to remove from this inventory: ")
        #Check if the item exists and remove it if it does. if it doesn't, print the following
        print("That item doesn't exist.")



#Inputs for Character Creation
new_name = input("Name for the new character?: ")
#Print the available races here
new_race = input("What race do you want?: ")

user_stat_choice = choice_input(["set", "generate"], "Do you want to set your own stats or generate random ones?(set/generate): ")
match user_stat_choice:
    case "set":
        pass
        #put the thing where it lets the user set stats. Not going to make inputs here yet.
    case "generate":
        pass
        #put the thing where we can generate values here

print("Setting Inventory for the new character")        #replace placeholder with character name once it's accessible
#While true loop here once the ability to actually add items to inventory is available
new_item = u_input('Type the item you want to add to this inventory(Type "done" to exit): ')
#break out of the while true loop once user says they're done
print("Type the level of [character name]")          #replace placeholder with character name once it's accessible
new_char_lvl = int_input()