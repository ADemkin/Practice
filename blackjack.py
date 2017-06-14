# coding: utf-8
#
#   Практическое задание курса "Основы Программирования" на GeekBrains.ru
#   Выполняю на Python 3.6.0, так интереснее :-)
#   BlackJack game by Anton Demkin, 2017
#   v1.0

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

def gameEnd():
    exit()


def getStatus():
    print('Dealer: %s (%d). Player: %s (%d).' % (" ".join(dealer), getSum(dealer),
                                                 " ".join(player), getSum(player)))
    # status for both
    if getSum(player) == getSum(dealer) == 21:
        print('Tie. Nobody wins.')
        gameEnd()
    
    # status for player
    if getSum(player) == 21:
        print('BLACKJACK! You win.')
        gameEnd()
    elif getSum(player) > 21:
        print('You loose.')
        gameEnd()
    # status for dealer
    if getSum(dealer) == 21:
        print('Dealer has blackjack! Dealer win.')
        gameEnd()
    if getSum(dealer) > 21:
        print('You win! Dealer lost.')
        gameEnd()


def offerCard():
    '''
    Offers player a new card. If player takes it- card gets added to player card list, sum gets calculated and updated.
    If no- function exits.
    '''
    if getSum(player) >= 21:
        getStatus()
    answer = ''
    while answer not in acceptable:
        answer = input('Do you want to take a card? y/n: ')
        if answer in acceptable:
            if answer in yes:
                print('Dealer gives you one more card.')
                player.append(getRandomCard())
            if answer in no:
                print('No more cards')
                break
            if answer in quit_program:
                gameEnd()
    getStatus()
        


def main():
    # start
    dealer.append(getRandomCard())
    player.append(getRandomCard())
    player.append(getRandomCard())
    if getSum(player) == 21:
        print('Holy shit! Blackjack! You win.')
        gameEnd()
    # basic status
    getStatus()

    if getSum(player) >= 21:
        getStatus()
    answer = ''
    while answer not in acceptable:
        answer = input('Do you want to take a card? y/n: ')
        if answer in acceptable:
            if answer in yes:
                print('Dealer gives you one more card.')
                player.append(getRandomCard())
            if answer in no:
                print('No more cards')
                break
            if answer in quit_program:
                gameEnd()
    # getStatus()
    while getSum(dealer) < 17:
        print("Dealer takes one more card.")
        dealer.append(getRandomCard())
    getStatus()
    if getSum(dealer) > getSum(player):
        print('Dealer wins!')
    else:
        print('Player wins!')
    gameEnd()
    
    
    
    
    # сначала игроку дают две карты
    # првоерка на автоматический блэкджэк
    # пока у игрока меньше 21 очка: игрок может взять еще одну карту или отказаться
    # в игру вступает дилер
    # дилер должен брать карты до тех пор, пока у него не будет 17 и более очков

if __name__ == "__main__":
    main()

'''
TODO:
1- раунды, счетчик раундов и возможность играть без перезагрузки игры
2- реальную колоду, чтобы не оказалось сгенерировано 5 тузов :D

'''