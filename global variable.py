#!/usr/bin/env python3
# coding: utf-8
#

counter = 0


def inc():
    global counter
    counter += 1
    return counter


def inc_silent():
    global counter
    counter += 1


[print(inc()) for i in range(10)]

[inc_silent() for i in range(10)]
print('')
[print(inc()) for i in range(10)]
