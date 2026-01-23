def u_input():
    return input('> ').lower().strip()
def int_input(max = 100000):
    while True:
        num = u_input()
        try:
            int(num)
        except:
            print('Input is not a number!')
        if num <= max:
            return num
        else:
            print('Input is too high!')
