from random import randint



def main():
    wins = 0
    
    while True:
        if randint(0, 6) < 1:
            print('the end')
            break
        else:
            wins += 1
    print('i have won ' + str(wins) + ' rounds')


if __name__ == "__main__":
    main()
