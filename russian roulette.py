from random import randint

'''
yes = ['y', 'Y', 'yes', 'Yes']
no = ['n', 'N', 'no', 'No']
quit = ['q', 'quit', 'Quit','exit', 'Exit']
acceptable = yes+no+quit
'''

def main():
    print('Welcome to Russian Roulette game! \nYou have only 1/6 chance to win!')
    input('Player turn first. Press enter to shoot.')
    for i in range(0,6):
        input('BANG!')
        if randint(0,6-i) < 1:
            print('YOU ARE DEAD!')
            exit()
        else:
            for j in range(0,6):
                if j > i:
                    print('[#]', end='')
                else:
                    print('[ ]', end='')
            print('\nYou are still alive. Now its your opponent turn...')




