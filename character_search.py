from helper import u_input
from helper import choice_input

#character search
def search(character_index):
    #get query
    query = u_input('Search by name, role, or race: ').title().strip()
    potentials = []
    #check for query in character names, race, and class
    for name in character_index.keys():
        char = character_index[name]
        #if the query was exactly the name of a character, return that character
        if query == name:
            return query
        #if its not a name, append it to potentials if its either a race or a class
        elif query == char.race.title(): #check each of the requirements
            potentials.append(name)
        elif query == char.role.title():
            potentials.append(name)

    #if there were no results, show that no characters matched
    if not potentials:
        print("No characters match your search!")
        return None

    #display matched characters and ask for choice
    for i, char in enumerate(potentials, 1):
        print(f'{i}: {char.capitalize()}')
    #make everything strings to prevent issues later
    options = potentials + [str(i) for i in range(1, len(potentials)+1)]
    choice = choice_input(options, "Type the number corresponding to the character to select a character: ")

    if choice in potentials:
        return choice
    elif choice.isdigit():
        return potentials[int(choice)-1]