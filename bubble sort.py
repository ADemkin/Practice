#!/usr/bin/env python3
# coding: utf-8
#
# Anton Demkin, 2017
# antondemkin@yandex.ru
#

from random import randint

unsorted = [randint(0, 100) for i in range(150)]


def bubble_sort(arr):
    '''
    Simplest bubble sort ever.
    '''
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr


def advanced_bubble_sort(arr):
    '''
    Little more advanced bubble sort.
    Quit cycle if already sorted.
    '''
    sorted_length = 0
    for iteration in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if sorted_length == len(arr):
                break
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_length = 0
            else:
                sorted_length += 1
    
    return arr


def bubble_sort_bigOh(arr):
    '''
    Simplest bubble sort.
    Returns some info for algorithm big Oh analysing:
    sorted array, number of operations, array length and worst case scenario.
    '''
    steps = 0
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            steps += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr, 'steps:', steps, 'array:', len(arr), 'worst case:', len(arr[1:]) ** 2


def advanced_bubble_sort_bigOh(arr):
    '''
    More advanced bubble sort.
    Returns some info for algorithm big Oh analysing:
    sorted array, number of operations, array length and worst case scenario.
    '''

    steps = 0
    sorted_length = 0
    for iteration in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if sorted_length == len(arr):
                break
            steps += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_length = 0
            else:
                sorted_length += 1
    
    return arr, 'steps:', steps, 'array:', len(arr), 'worst case:', len(arr[1:]) ** 2



def bubble_sort_isoteric(arr):
    prev_item = arr[0]
    for i in range(1,len(arr)):
        if prev_item > item:
            prev_item, item = item, prev_item
        else:
            prev_item = item
    return arr


# print(unsorted)
# print(advanced_bubble_sort_bigOh(unsorted))
# print(bubble_sort_bigOh(unsorted))

print(bubble_sort_isoteric([5,3,4,6,0,2,1]))