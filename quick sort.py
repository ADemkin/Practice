#!/usr/bin/env python3
# coding: utf-8
#

from arraygen import genArray

unsorted = genArray(50, 0, 100)


def quick_sort(list):
    # base case
    if len(list) == 0:
        return []
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        if list[1] < list[0]:
            list[1], list[0] = list[0], list[1]
        return list
    # main logic
    else:
        # переменные
        lower = []
        higher = []
        base = list[0]
        # раскидываем значения по двум спискам
        for i in list[1:len(list)]:
            if i < base:
                lower.append(i)
                # lower += [i]
            if i >= base:
                higher.append(i)
                # higher += [i]
                # higher.extend(i)
        
        # создаем пустой новый список, к кторому будут присоединены все последующие
        newlist = []
        # костыль, пока не понял как это сделать правильно. TODO: спросить Олега или Игоря как это делать правильно!
        newlower = quick_sort(lower)
        newhigher = quick_sort(higher)
        
        if type(newlower) == int:
            newlist.append(newlower)
        else:
            newlist += newlower
        
        newlist.append(base)
        
        if type(newhigher) == int:
            newlist.append(newhigher)
        else:
            newlist += newhigher
        # конец костыля
        # ну хоть работает как надо :D TODO: исправить костыль
        
        # возвращаем список
        return newlist
        
        # not working!!!
        # return quick_sort(lower) + [base] + quick_sort(higher)


print(quick_sort([5, 8, 3, 1, 19, 2, 4, 22, 0, 55]))
