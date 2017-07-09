#!/usr/bin/env python3
# coding: utf-8
#


from arraygen import genArray
from random import randint


def quick_sort(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    if len(arr) >= 3:
        base = arr[0]
        lower = [i for i in arr[1:] if i < base]
        higher = [i for i in arr[1:] if i >= base]
        return quick_sort(lower) + [base] + quick_sort(higher)


def shuffle(arr):
    '''
    Забираем линейно, добавляем случайно.
    '''
    newArr = []
    length = len(arr)
    taken = []
    
    # iterate through all elements in array
    for i in range(length):
        # generate random index
        randomIndex = randint(0, length)
        
        # if index already in use, get new one
        # todo: optimise left and right border here
        while randomIndex in taken:
            randomIndex = randint(0, length)
        
        # if not in use, add to used list
        taken.append(randomIndex)
        
        # transfer value from one list to another
        newArr.insert(randomIndex, arr[i])
    # end
    return newArr

# tests:

array = genArray(5000, 0, 10000, True)

# print(array)

shuffed = shuffle(array)

# print(shuffed)

sorted = quick_sort(shuffed)

# print(sorted)

print("Original is the same as shuffled then sorted: " + str(sorted == array))

# working!
