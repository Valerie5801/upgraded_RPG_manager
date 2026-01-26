#AS 2nd character creation for RPG character manager
import random
from helper import u_input
character_index = {}

def character_create(character_index):

    def stat_gen():
        stat_1 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
        stat_1.remove(min(stat_1))
        stat_1 = sum(stat_1)
        stat_2 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
        stat_2.remove(min(stat_2))
        stat_2 = sum(stat_2)
        stat_3 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
        stat_3.remove(min(stat_3))
        stat_3 = sum(stat_3)
        stat_4 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
        stat_4.remove(min(stat_4))
        stat_4 = sum(stat_4)
        return [stat_1, stat_2, stat_3, stat_4]
    
    def check(input, character_index):
        if input in character_index:
            return True
        else:
            return False
    
    while not False:
        name = u_input("What is your character's name? ").title()
        if check(name, character_index) == False:
            character_index[name] = {}
            break
        else:
            print("You already have a character with that name. Please try again.")
            continue