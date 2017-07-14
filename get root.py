# Anton Demkin, 2017


def get_root_low_accuracy(number):
    '''
    не самая красивая вариация, сравнение чисел выполнено не совсем корректно.
    '''
    # lower = faster, higher = more accurate
    accuracy = 14
    lowest = 0
    highest = number
    middle = (lowest + highest) / 2
    while round( middle ** 2, accuracy) != number:
        if middle ** 2 > number:
            highest = middle
        if middle ** 2 < number:
            lowest = middle
        middle = (lowest + highest) / 2
    
    return middle
    
    

# print(get_root_low_accuracy(16) == 4)
# print(get_root_low_accuracy(64) == 8)
# print(get_root_low_accuracy(1024) == 32)
#
# print(get_root_low_accuracy(5645479128))

def get_root(number):
    '''
    Гораздо точнее, используется корректное сравнение float значений
    '''
    # high accuracy
    eps = 0.000000000000001
    # high speed
    #eps = 0.000000001
    low = 0
    high = number
    root = (low + high) / 2
    while abs(root ** 2 - number) > eps:
        # binary search
        if root ** 2 > number:
            high = root
        if root ** 2 < number:
            low = root
        root = (low + high) / 2
        #print(root)
    return root


#print(get_root(35) ** 2)
#print(get_root(74) ** 2)
#print(get_root(123) ** 2)

def get_root_faster(number):
    eps = 0.00000000000001
    low = 0
    high = number
    root = ( low + high ) / 2
    while abs(low - high) > eps:
        if root ** 2 > number:
            high = root
        if root ** 2 < number:
            low = root
        root = ( low + high ) / 2
    return root


# print(get_root_faster(35), get_root(35))
# print(get_root_faster(36), get_root(36))
