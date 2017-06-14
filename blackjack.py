# coding: utf-8
#
#   Практическое задание курса "Основы Программирования" на GeekBrains.ru
#   Выполняю на Python 3.6.0, так интереснее :-)
#   BlackJack game by Anton Demkin, 2017
#

from random import randint

yes = ['y', 'Y', 'yes', 'Yes']
no = ['n', 'N', 'no', 'No']
quit_program = ['q', 'quit_program', 'Quit', 'exit', 'Exit']
acceptable = yes + no + quit_program

cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
dealer = list()
player = list()


def getRandomCard():
    '''
    generates a random card
    '''
    return cards[randint(0, len(cards) - 1)]


def getSum(array):
    '''
    calculates best value of cards

    '''
    sum = 0
    # get sum without Aces
    for i in array:
        if i == 'J' or i == 'Q' or i == 'K':
            sum += 10
        elif i == 'A':
            continue
        else:
            sum += int(i)
    
    # now calculate Aces with 11 or 1, depending on a better value
    for i in array:
        if i == 'A':
            if sum > 10:
                sum += 1
            else:
                sum += 11
    return sum


def getStatus():
    print('Dealer: %s (%d). Player: %s (%d).' % (" ".join(dealer), getSum(dealer),
                                                 " ".join(player), getSum(player)))


def offerCard():
    '''
    Offers player a new card. If player takes it- card gets added to player card list, sum gets calculated and updated.
    If no- function exits.
    '''
    answer = ''
    while answer not in acceptable:
        answer = input('Do you want to take a card? y/n: ')
        if answer in acceptable:
            if answer in yes:
                print('One more card')
                player.append(getRandomCard())
            if answer in no:
                print('No more cards')
            if answer in quit_program:
                break
        getStatus()
        


def main():
    # start
    dealer.append(getRandomCard())
    player.append(getRandomCard())
    player.append(getRandomCard())
    # basic status
    getStatus()
    offerCard()


if __name__ == "__main__":
    main()
