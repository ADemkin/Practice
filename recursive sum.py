#!/usr/bin/env python3
# coding: utf-8
#

from random import randint
from arraygen import genArray

random_list = genArray(10, 0, 15)
print(random_list)


def recursive_sum(list):
    if len(list) == 1:
        return list[0]
    sum = list[0] + recursive_sum(list[1:len(list)])  # не забывать, как работает нарезка списка!
    return sum


#just to check myself
def cycle_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


print(recursive_sum(random_list))
print(cycle_sum(random_list))


