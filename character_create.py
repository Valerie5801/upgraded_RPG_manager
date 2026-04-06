#AS 2nd character creation for RPG character manager
import random
from helper import u_input, choice_input, int_input
from user_inputs import input_inventory
from skill_management import level_up
from classes import Character, RandomGenerator
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
        
    
    name = ""
    new_race = ""
    class_choice = ""
    char_back = ""

    #get character name
    print("Do you want to set the name, race, class, and backstory of your character or have it generated?")
    print('Please type either "set" or "generate"')
    set_or_gen = choice_input(["set", "generate"])
    match set_or_gen:
        case "set":
            while True:
                name = u_input("What is your character's name?: ").title().strip()
                if name not in character_index:
                    break
                else:
                    print("You already have a character with that name. Please try again.")
    
            #get character race
            print(f"Here are the available races: {', '.join(races)}")
            new_race = choice_input(races,f"What is {name.capitalize()}'s race?: ")

            #get character class
            print(f"Here are the available classes: {', '.join(classes)}")
            class_choice = choice_input(classes,f"What is {name.capitalize()}'s class?: ")

            #ask user if they want to make a backstory about their character.
            ask_backstory = choice_input(["yes", "no"], f"Do you want to add a backstory for {name.capitalize()}?: ")
            if ask_backstory == "yes":
                print(f"Type {name.capitalize()}'s backstory and press ENTER when done.")
                char_back = input("> ")
            else:
                char_back = "No backstory here yet!"

        case "generate":
            print("Please note that the backstory will be a random selection of words!")
            gen_info = RandomGenerator()
            name = gen_info.name
            new_race = gen_info.race
            class_choice = gen_info.role
            char_back = gen_info.backstory
            print(f"Name: {name}\nRace: {new_race}\nClass: {class_choice}\nBackstory: {char_back}")
            
    #create character object using Character class
    new_char = Character(name.title(), new_race, class_choice, char_back)

    #get initial inventory. edited to work with the Character class
    print(f"\nSetting {new_char.name}'s inventory...")
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
    new_char.split_skill_pts(stat_list)

    #display final stats
    print('\nHere are your final stats:')
    print(new_char)
    return new_char