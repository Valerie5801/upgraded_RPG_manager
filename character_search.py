from helper import u_input
from helper import choice_input

#character search
def search(character_index):
    #get query
    query = u_input('Search by name, level, race, or class: ')
    potentials = []
    #check for query in character names, levels, race, and class
    for name in character_index.keys():
        char = character_index[name]
        if query == name:
            potentials.append(name)
        elif query == str(char.level):
            potentials.append(name)
        elif query == char.race: #race
            potentials.append(name)
        elif query == char.role: #class
            potentials.append(name)
    #if it found the example character, remove it
    if 'example' in potentials:
        potentials.remove('example')

    #if the query was exactly the name of a character, return that character
    if query in potentials:
        return query
    
    #if there were no results, use example character
    if not potentials:
        print("No characters match search! Using example character.")
        return 'example'
    index = 0

    #display matched characters and ask for choice
    for char in potentials:
        index += 1
        print(f'{index}: {char.capitalize()}')
    choice = choice_input(potentials + list(range(1,index+1)), "Type the name of the character you want to view: ")
    if choice in potentials:
        return choice
    elif choice in list(range(1,index+1)):
        return potentials[choice-1]

