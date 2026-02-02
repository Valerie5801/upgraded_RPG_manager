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