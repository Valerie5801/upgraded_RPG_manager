def u_input(prompt = '> '):
    return input(prompt).lower().strip()
def int_input(max = 100000,prompt='> '):
    while True:
        num = u_input(prompt)
        try:
            num = int(num)
        except:
            print('Input is not a number!')
            continue
        if num <= max:
            return num
        else:
            print('Input is too high!')
def choice_input(choices,prompt = '> '):
    while True:
        choice = u_input(prompt)
        if choice in choices:
            return choice
        else:
            print('Please select a valid choice!')
int_input()