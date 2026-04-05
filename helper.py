import csv
import json
from char_classes import Character

#user input
def u_input(prompt = '> '):
    return input(prompt).lower().strip()
#number input
def int_input(max = 100000,prompt='> ',min = 0):
    while True:
        num = u_input(prompt)
        try:
            num = int(num)
        except:
            print('Input is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('Input is out of range!')
#input from choices
def choice_input(choices,prompt = '> '):
    while True:
        choice = u_input(prompt)
        if choice in choices:
            return choice
        else:
            print('Please select a valid choice!')


#function to save the CSV for first time when program is ran
def save_csv():
    #try the following:
    try:
        character_index = {}

        with open("docs/characters.csv", mode="r", newline="") as file:
            #use dictionary reader
            reader = csv.DictReader(file)

            for row in reader:
                #make character layout/format
                char = Character(
                    row["Name"],
                    row["Race"],
                    row["Class"],
                    row["Backstory"],
                    #add back numbers
                    int(row["Level"]),
                    int(row["Skill Points"]),

                    #add back the values that are lists and dictionaries
                    json.loads(row["Stats"]),
                    json.loads(row["Skills"]),
                    json.loads(row["Inventory"])
                )

                #store in dictionary
                character_index[char.name] = char

    except FileNotFoundError:
        #tell the CSV doesn't exist and return an empty dict
        print("The CSV doesn't exist.")
        return {}
    
    else:
        return character_index
    

#function for rewriting the CSV again. This will be used every time the user makes a change to their library:
def rewrite_csv(characters):
    with open("docs/characters.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)   #read through list
        #write the header
        writer.writerow(['Name','Race','Class','Level','Skill Points','Skills','Inventory','Description','Backstory','Personality Traits'])
        
        #loop through students
        for character in characters.values():
            row = [
                character.name,
                character.race,
                character.role,
                character.level,
                character.skill_points,
                json.dumps(character.skills),
                json.dumps(character.inventory),
                character.backstory,
                """json.dumps(character.personality_traits)"""
            ]
            #write a row.
            writer.writerow(row)