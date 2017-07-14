#!/usr/bin/env python3
# coding: utf-8
#

from arraygen import genArray


def quick_sort(list):
    # base case
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list[0]]  # bug was here: new return list always
    # swap if needed
    elif len(list) == 2:
        if list[1] < list[0]:
            list[1], list[0] = list[0], list[1]
        return list
    # main logic
    else:
        # переменные
        base = list[0]
        
        # новый вариант через list comprehension, спасибо Олегу за подсказку.
        higher = [i for i in list[1:] if i >= base]
        lower = [i for i in list[1:] if i < base]
        
        # # создаем пустой новый список, к кторому будут присоединены все последующие
        # newlist = []
        # # костыль, пока не понял как это сделать правильно. TODO: спросить Олега или Игоря как это делать правильно!
        # newlower = quick_sort(lower)
        # newhigher = quick_sort(higher)
        # # append left part
        # if type(newlower) == int:
        #     newlist.append(newlower)
        # else:
        #     newlist += newlower
        # # append base part
        # newlist.append(base)
        # # append higher part
        # if type(newhigher) == int:
        #     newlist.append(newhigher)
        # else:
        #     newlist += newhigher
        # # конец костыля
        # # ну хоть работает как надо :D TODO: исправить костыль
        #
        # # возвращаем список
        # return newlist
        
        # not working!!!
        # update: Не работает даже после изменения кода фильтра. Почему не хочет складывать list и [int]?
        # update: Проблема не в [base], а в том, что рекурсивный вызов можат вернуть не список, а int.
        # update: заработало после того, как принудительно стал возвращать list в случае одного элемента!
        return quick_sort(lower) + [base] + quick_sort(higher)


# print(quick_sort([5, 8, 3, 1, 19, 2, 4, 22, 0, 55, 34, 6, 42, 12]))
# print(quick_sort(genArray(100,0,1000, False)))



def quick_sort_again(arr):
    '''
    Еще раз по памяти, без подглядывания.
    '''
    # рассмотрим базовые случаи
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    # меняем элементы массива местами, если нужно
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    # фильтруем и соединяем
    if len(arr) >= 3:
        base = arr[0]
        lower = [i for i in arr[1:] if i < base]
        higher = [i for i in arr[1:] if i >= base]
        return quick_sort_again(lower) + [base] + quick_sort_again(higher)


# check
print(quick_sort_again([5, 8, 3, 1, 19, 2, 4, 22, 0, 55, 34, 6, 42, 12]))
#print(quick_sort_again(genArray(100, 0, 1000, False)))

