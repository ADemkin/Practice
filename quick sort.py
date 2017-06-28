#!/usr/bin/env python3
# coding: utf-8
#

from arraygen import genArray

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
        base = list[0]
 
        # новый вариант через list comprehension, спасибо Олегу за подсказку.
        higher = [ i for i in list[1:len(list)] if i >= base]
        lower = [i for i in list[1:len(list)] if i < base]
        
        
        # создаем пустой новый список, к кторому будут присоединены все последующие
        newlist = []
        # костыль, пока не понял как это сделать правильно. TODO: спросить Олега или Игоря как это делать правильно!
        newlower = quick_sort(lower)
        newhigher = quick_sort(higher)
        # append left part
        if type(newlower) == int:
            newlist.append(newlower)
        else:
            newlist += newlower
        # append base part
        newlist.append(base)
        # append higher part
        if type(newhigher) == int:
            newlist.append(newhigher)
        else:
            newlist += newhigher
        # конец костыля
        # ну хоть работает как надо :D TODO: исправить костыль

        # возвращаем список
        return newlist

        # not working!!!
        # update: Не работает даже после изменения кода фильтра. Почему не хочет складывать list и [int]?
        #return quick_sort(lower) + [base] + quick_sort(higher)


print(quick_sort([5, 8, 3, 1, 19, 2, 4, 22, 0, 55, 34, 6, 42, 12]))
print(quick_sort(genArray(400,0,1000, False)))
