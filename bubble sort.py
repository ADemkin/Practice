#!/usr/bin/env python3
# coding: utf-8
#
# Anton Demkin, 2017
# antondemkin@yandex.ru
#

from random import randint

unsorted = [randint(0, 100) for i in range(15)]


def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr


print(unsorted)
print(insertion_sort(unsorted))
