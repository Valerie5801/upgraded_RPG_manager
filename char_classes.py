#VY 2nd classes for upgraded rpg manager
from helper import choice_input

#DataVizualization class (use Matplotlib and/or Pandas)
class DataVizualization:
    pass

#StatisticalAnalyzer class (use Matplotlib)
class Statisticalanalyzer:
    pass

#RandomGenerator class (use Faker)
class RandomGenerator:
    pass

#Characters class (parent class)
class ExistCharacters:
    def __init__(self, char_list = None):
        if char_list:
            self.char_list = char_list
        else:
            self.char_list = []

    #method to add students
    def add_char(self, student):
        self.char_list.append(student)

    #method to remove students
    def remove_char(self, character):
        if character in self.char_list:
            self.char_list.remove(character)
        else:
            print("That character doesn't exist.")

    #method to show all students
    def show_chars(self):
        for char in self.char_list:
            print(char)

    #method to return information
    def save_info(self):
        return self.char_list

#Character class (for character creation and character object management)
class Character:
    def __init__(self, name, race, role, backstory):  #using "role" as a substitute word for "class"
        self.name = name.capitalize()
        self.level = 1  #level should stay 1 since it's a new character
        self.race = race.strip().lower()
        self.role = role.strip().lower()
        self.backstory = backstory
        self.inventory = []
        #set all stats to 0
        self.stats = {
            'strength': 0,
            'dexterity': 0,
            'resilience': 0,
            'magic': 0,
        }
        #empty set for skills
        self.skills = dict()
        #automatically gives three skill points
        self.skill_points = 3

        #give racial bonuses and specific-skills based on race
        if self.race == "human":
            self.stats = {
                'strength': 1,
                'dexterity': 1,
                'resilience': 1,
                'magic': 1
            }
        elif self.race == "orc":
            self.stats = {
                'strength': 2,
                'dexterity': 0,
                'resilience': 1,
                'magic': 0
            }
            self.skills = {'physical attack': 0}
        elif self.race == "elf":
            self.stats = {
                'strength': 0,
                'dexterity': 2,
                'resilience': 0,
                'magic': 1,
            }
            self.skills = {'buff magic': 0}
        elif self.race == "dwarf":
            self.stats = {
                'strength': 1,
                'dexterity': 0,
                'resilience': 2,
                'magic': 0
            }
            self.skills = {'defense boost': 0}


    #method that sets skills based on race
    def split_skill_pts(self, value_list):
        remaining = {'strength','dexterity','magic','resilience'}
        for stat in value_list:
            display_remaining = ', '.join([i.title() for i in remaining])
            if len(remaining) > 1:
                print(f'What stat do you want the value {stat} to be? ({display_remaining})')
                to_place = choice_input(remaining)
            else:
                print(f'Assigned {stat} to {display_remaining}')
                to_place = list(remaining)[0]
            #ensure that the to_place value doesn't full on replace the existing stats (since they are racial bonuses before the main stats)
            self.stats[to_place] += int(stat)
            remaining.remove(to_place)


    #method to level up
    def level_up(self):
        pass


    #method to add a new skill/ability
    def add_skill(self):
        pass


    #method to reset skill points
    def reset_skill_pts(self):
        pass


    #method to add an item to the inventory
    def add_inventory(self, item):
        self.inventory.append(item)


    #method to remove an item to the inventory
    def remove_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item.capitalize()} successfully removed from inventory.\n")
        else:
            print(f"{item.capitalize()} not found.")


    #method to edit the personal information for the character (name, description, backstory, and persona_traits)
    def edit_info(self):
        pass


    #method to return information as a dictionary
    def return_info(self):
        #make a dictionary with all the info
        self.info = {'Name': self.name, 
                    'Race': self.race, 
                    'Class': self.role}
        #add the grades to the info dictionary
        self.info.update(self.stats)
        return self.info


    #method to print out the information of the character (will be used in the "view character" option of the menu)
    def __str__(self):
        show_stats = ""
        for stat in self.stats.keys():
            show_stats += f'\t{stat}: {self.stats[stat]}\n'
        show_info = f"Here is the information about {self.name}:" + f"Name: {self.name}\nRace: {self.race}\nClass: {self.role}\nStats:" + show_stats
        return show_info