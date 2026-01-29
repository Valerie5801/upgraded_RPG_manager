from helper import u_input
from helper import choice_input
def search(character_index):
    query = u_input('Search: ')
    potentials = []
    for name in character_index.keys():
        char = character_index[name]
        if query in name:
            potentials.append(name)
        elif query in str(char['level']):
            potentials.append(name)
        elif query in char['key info'][0]:
            potentials.append(name)
        elif query in char['key info'][1]:
            potentials.append(name)
    if 'example' in potentials:
        potentials.remove('example')
    if not potentials:
        print("No characters match search! Using example character.")
        return 'example'
    index = 0
    for char in potentials:
        index += 1
        print(f'{index}: {char}')
    choice = choice_input(potentials + list(range(1,index+1)))
    if choice in potentials:
        return choice
    elif choice in list(range(1,index+1)):
        return potentials[choice-1]

