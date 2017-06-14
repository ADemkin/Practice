from random import randint

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
    # dealer = ['Q']
    # player = ['A']
    print('Dealer: %s (%d). Player: %s (%d).' % (" ".join(dealer), getSum(dealer),
                                                 " ".join(player), getSum(player)))


def main():
    dealer.append(getRandomCard())
    player.append(getRandomCard())
    player.append(getRandomCard())
    
    # print(dealer, player)
    getStatus()


if __name__ == "__main__":
    main()
