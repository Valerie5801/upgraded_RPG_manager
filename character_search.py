from helper import u_input
from helper import choice_input
def search(character_index):
    query = u_input('Search: ')
    potentials = []
    for name in character_index.keys():
        char = character_index[name]
        if query in name:
            potentials.append(name)
        elif query in char['level']:
            potentials.append(name)
        elif query in char['race']:
            potentials.append(name)
        elif query in char['class']:
            potentials.append(name)
    #not finished! Dont use this yet!
    