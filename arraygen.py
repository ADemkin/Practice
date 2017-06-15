'''
this script generates am array of given length and range
'''

from random import randint


def genArray(length=100, rangeMin=0, rangeMax=255):
    list = []
    for i in range(0, length):
        list.append(randint(rangeMin, rangeMax))
    return list


def main():
    for i in range(0, 2):
        print(genArray(100))


if __name__ == "__main__":
    main()
