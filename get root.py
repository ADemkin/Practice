# Anton Demkin, 2017


def get_root(number):
    # lower = faster, higher = more accurate
    accuracy = 5
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
    
    

print(get_root(16) == 4)
print(get_root(64) == 8)
print(get_root(1024) == 32)

print(get_root(5645479128))