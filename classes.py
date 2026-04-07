#VY 2nd classes for upgraded rpg manager
from helper import choice_input
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#DataVizualization class (use Matplotlib and/or Pandas)
class DataVizualization:
    #initialize
    def __init__(self, df):
        self.df = df

    #method to plot said data frame
    def bar_stat(self, name):
        stat_columns = ['strength', 'dexterity', 'resilience', 'magic']

        row = self.df[self.df['Name'] == name]
        #sanitization
        if row.empty:
            return "Character not found."
        
        #get the specific row
        row = row.iloc[0]
        #get the values for the stats
        values = [row[stat] for stat in stat_columns]

        plt.figure()
        #make the graph and plot out the values.
        plt.bar(stat_columns, values)
        plt.title(f"{name}'s Stats")
        plt.xlabel("Stats")
        plt.ylabel("Value")

        plt.show() #use this one when submitting/non codespace

    #method to make a radar graph
    def radar_chart(self, name):
        #strength will be up, dexterity right, resilience down, magic left
        stat_columns = ['strength', 'dexterity', 'resilience', 'magic']

        row = self.df[self.df['Name'] == name]
        #sanitization
        if row.empty:
            return "Character not found."

        #get the specific row
        row = row.iloc[0]
        #get each of the stats
        values = [row[stat] for stat in stat_columns]
        #close the polygon
        values += values[:1]

        #get angles for each stat and end it with the first value to close the polygon
        angles = np.linspace(0, 2 * np.pi, len(stat_columns), endpoint=False).tolist()
        angles += angles[:1]

        plt.figure()

        #draw the circular radar grid
        ax = plt.subplot(111, polar=True)
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)

        #label the axis
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(stat_columns)

        #title it
        plt.title(f"{name}'s Stat Profile")

        plt.show()

    #method to make a graph that compares two people's stats
    def compare_stat(self, stat, names_list):
        #get the row from the datafram for the characters
        selected = self.df[self.df['Name'].isin(names_list)]
        #sanitization
        if selected.empty:
            return "No matching characters found."

        #as a failsafe, make a new graph
        plt.figure()

        plt.bar(selected['Name'], selected[stat])
        plt.title(f"{stat.capitalize()} stat Comparison")
        plt.xlabel("Characters")
        plt.ylabel(stat.capitalize())

        plt.tight_layout()

        plt.show()


#StatisticalAnalyzer class (use Pandas)
class StatisticalAnalyzer:
    #initialize with characters
    def __init__(self, characters):
        self.characters = characters
        self.df = self.build_dataframe()

    #method for building a data frame
    def build_dataframe(self):
        data = []

        for char in self.characters.chars.values():
            #call the method that gets all the character data
            data.append(char.return_info())

        #put all the data in a table
        self.df = pd.DataFrame(data)
        return self.df

    #method to get character stats and find their strongest/weakest areas
    def get_character_profile(self, name):
        #get the specific row of the dataframe that includes the character's name
        row = self.df[self.df['Name'] == name]

        #if the character doesn't exist
        if row.empty:
            #say that character wasn't found
            return f"{name} doesn't exist."

        #get row 0
        row = row.iloc[0]

        stat_columns = ['strength', 'dexterity', 'resilience', 'magic']

        #dictionary of the character's stats
        stats = {stat: row[stat] for stat in stat_columns}

        #get the highest and lowest stats
        highest_stat = max(stats, key=stats.get)
        lowest_stat = min(stats, key=stats.get)

        #return the dictionary of this info
        return {
            "name": name,
            "stats": stats,
            "specialty": highest_stat,
            "weakness": lowest_stat
        }

    #method to get the mean, min, max, and median of all the existing characters
    def stat_summary(self):
        stats_columns = ['strength', 'dexterity', 'resilience', 'magic']

        #use built-in function and put it in a dictionary
        summary = {
            "mean": self.df[stats_columns].mean(),
            "min": self.df[stats_columns].min(),
            "max": self.df[stats_columns].max(),
            "median": self.df[stats_columns].median()
        }

        #return the dictionary
        return summary

    #method to compare two different characters on their stats
    def compare_chars(self, first_name, second_name):
        stat_columns = ['strength', 'dexterity', 'resilience', 'magic']
        comparison_list = []   
        #get the stats of the first and second character
        first_profile = self.get_character_profile(first_name)
        second_profile = self.get_character_profile(second_name)

        #sanitization
        if isinstance(first_profile, str) and not isinstance(second_profile, str):
            return f"{first_name} doesn't exist."
        elif not isinstance(first_profile, str) and isinstance(second_profile, str):
            return f"{second_name} doesn't exist."
        elif isinstance(first_profile, str) and isinstance(second_profile, str):
            return f"Both characters do not exist."
        
        first_stats = first_profile['stats']
        second_stats = second_profile['stats']

        for stat in stat_columns:
            if first_stats[stat] > second_stats[stat]:
                comparison_list.append(f"{first_name} has a greater {stat.capitalize()} stat than {second_name}.")
            elif first_stats[stat] < second_stats[stat]:
                comparison_list.append(f"{first_name} has a smaller {stat.capitalize()} stat than {second_name}.")
            else:
                comparison_list.append(f"{first_name} has the same {stat.capitalize()} stat as {second_name}.")
        return comparison_list


#RandomGenerator class (use Faker)
class RandomGenerator:
    def __init__(self):
        self.fake = Faker()
        self.name = self.fake.first_name()
        self.race = self.fake.random_element(elements=['human', 'orc', 'elf', 'dwarf'])
        self.role = self.fake.random_element(elements=['cleric', 'wizard', 'fighter', 'rogue'])
        self.backstory = self.fake.sentence(nb_words = 12)


#Characters class (parent class)
class ExistCharacters:
    def __init__(self, chars = None):
        if chars is not None:
            self.chars = chars
        else:
            self.chars = {}

    #method to add characters
    def add_char(self, character):
        self.chars[character.name] = character

    #method to remove characters
    def remove_char(self, name):
        if name in self.chars.keys():
            del self.chars[name]
        else:
            print("That character doesn't exist.")

    #method to show all characters
    def show_chars(self):
        for char in self.chars.values():
            print(char)

    #method to return information
    def save_info(self):
        return self.chars


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

    #method to reset skill points
    def reset_skill_pts(self):
        #reset skills and add those skill points to unspent
        for i in self.skills.keys():
            self.skill_points += self.skills[i]
            self.skills[i] = 0

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

    #method to edit the personal information for the character (name, backstory)
    def edit_info(self, new_name, backstory):
        self.name = new_name
        self.backstory = backstory

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
        show_inventory = ""
        show_skills = ""
        for stat in self.stats.keys():
            show_stats += f'\t{stat}: {self.stats[stat]}\n'
        for item in self.inventory:
            show_inventory += f'\t-{item}\n'
        for skill in self.skills.keys():
            show_skills += f'\t{skill}: {self.skills[skill]}\n'
        show_info = f"\nHere is the information about {self.name}:\n" + f"Name: {self.name}\nRace: {self.race}\nClass: {self.role}\nStats:\n" + show_stats + f"\nLevel: {self.level}\nSkill Points: {self.skill_points}\nSkills:\n" + show_skills + "Inventory:\n" + show_inventory + f"Backstory: {self.backstory}\n"
        return show_info