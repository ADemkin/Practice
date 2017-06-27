#!/usr/bin/env python3
# coding: utf-8
#

from random import randint
from arraygen import genArray


random_length_list = genArray(randint(10,300))
# random_length_list = [0,1,2,3]

def recursive_counter(list):
    if list == []:
        return 0
    else:
        return len(list[0:len(list) - 1])



def cycle_counter(list):
    counter = 0
    for i in list:
        counter += 1
    return counter


print(recursive_counter(random_length_list))
print(recursive_counter(random_length_list))

