from helper import u_input
from helper import choice_input

#character search
def search(character_index):
    #get query
    query = u_input('Search by name, role, or race: ')
    potentials = []
    #check for query in character names, race, and class
    for name in character_index.keys():
        char = character_index[name]
        if query == name: #name
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

    #if there were no results, show that no characters matched
    if not potentials:
        print("No characters match your search!")
        return None

    #display matched characters and ask for choice
    for i, char in enumerate(potentials, 1):
        print(f'{i}: {char.capitalize()}')
    #make everything strings to prevent issues later
    options = potentials + [str(i) for i in range(1, len(potentials)+1)]
    choice = choice_input(options, "Type the name or number: ")

    if choice in potentials:
        return choice
    elif choice.isdigit():
        return potentials[int(choice)-1]