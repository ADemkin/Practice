#!/usr/bin/env python3
# coding: utf-8
#
# Anton Demkin, 2017
# antondemkin@yandex.ru
#

from random import randint

unsorted = [randint(0, 100) for i in range(40)]


def insertion_sort(array):
    maximum_value = max(array)
    for i in range(len(array)):
        lowest = maximum_value
        lowest_index = i
        for j in range(i, len(array)):
            if array[j] < lowest:
                lowest = array[j]
                lowest_index = j
        # swap
        array[i], array[lowest_index] = array[lowest_index], array[i]
    # done
    return array


print(insertion_sort(unsorted))
