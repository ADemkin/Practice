'''
this script generates am array of given length, range and it may sort it.
'''

from random import randint


def genArray(length=100, rangeMin=0, rangeMax=255, sorted = False):
    list = []
    for i in range(0, length):
        list.append(randint(int(rangeMin), int(rangeMax)))
    if sorted:
        list.sort()
    return list


def main():
    print(genArray(100))
    print(genArray(100,sorted=True))



if __name__ == "__main__":
    main()
