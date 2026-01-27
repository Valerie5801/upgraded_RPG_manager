#VY 2nd Menu
from helper import u_input

def main_menu():
    while True:
        print("You can: \n1. Create a Character \n2. Edit a Character \n3. View a Character \n4. Exit the Program(This will wipe all data!)")
        user_choice = input("Type the number that corresponds with the action that you want to perform: ").strip()
        
        match user_choice:
            case "1":
                #run character creation
                pass
            case "2":
                #when all other functions exist, put them here.
                pass
            case "3":
                #show character function here
                pass
            case "4":
                break
            case _:
                print("That isn't an option, please try again.")

print("This is a RPG Character Manager.")
main_menu()
print("Thank you for using the Character Manager.")