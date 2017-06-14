from random import randint


def main():
    rounds = 6
    while True:
        s = input('Enter yes to play. Enter nothing to quit if you a slacker. \n')
        if s == 'yes' or s == 'y':
            if randint(0, rounds) < 1:
                print("BANG! You're dead!")
                exit()
            else:
                rounds -= 1
                print("Click. You still alive. There are " + str(rounds) + " bullets left in barrel.")
        
        else:
            print("Poh poh poh! See ya, slacker!")
            break


if __name__ == "__main__":
    main()
