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
                    row["Backstory"]
                )

                    #add back numbers
                char.level = int(row["Level"])
                char.skill_points = int(row["Skill Points"])

                    #add back the values that are lists and dictionaries
                char.stats = json.loads(row["Stats"])
                char.skills = json.loads(row["Skills"])
                char.inventory = json.loads(row["Inventory"])

                #store in dictionary
                character_index[char.name] = char
            return character_index

    except FileNotFoundError:
        #tell the CSV doesn't exist and return an empty dict
        print("The CSV doesn't exist.")
        return {}
    

#function for rewriting the CSV again. This will be used every time the user makes a change to their library:
def rewrite_csv(characters):
    with open("docs/characters.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)   #read through list
        #write the header
        writer.writerow(['Name','Race','Class','Backstory','Level','Skill Points','Stats','Skills','Inventory'])
        
        #loop through students
        for character in characters.values():
            row = [
                character.name,
                character.race,
                character.role,
                character.backstory,
                character.level,
                character.skill_points,
                json.dumps(character.stats),
                json.dumps(character.skills),
                json.dumps(character.inventory)
            ]
            #write a row.
            writer.writerow(row)


#function for getting all characters' information into a list
def get_chars_info(character_index):
    data = []
    #loop through the characters
    for character in character_index.values():
        #call the method to bring all the information together into a dictionary
        data.append(character.return_info())
    #return character information
    return data