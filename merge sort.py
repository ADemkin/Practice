# Anton Demkin, 2017

from arraygen import genArray


def merge_sort(arr):
    '''
    Немного кривоватая реализация, но работает.
    TODO: Узнать у Олега или Игоря как написать красивее.
    '''
    # base case
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    # sort
    else:
        # define split point
        mid = len(arr) // 2
        
        # recursively sort lower and higher parts
        lower = merge_sort(arr[:mid])
        higher = merge_sort(arr[mid:])
        
        # merge two parts
        newArr = []
        lowerIndex = 0
        higherIndex = 0
        while len(newArr) < len(arr):
            # костыль для фильтрации выхода за пределы массива
            if lowerIndex > len(lower) - 1:
                newArr.append(higher[higherIndex])
                higherIndex += 1
            elif higherIndex > len(higher) - 1:
                newArr.append(lower[lowerIndex])
                lowerIndex += 1
            
            # собираем новый массив
            elif lower[lowerIndex] < higher[higherIndex]:
                newArr.append(lower[lowerIndex])
                lowerIndex += 1
            else:
                newArr.append(higher[higherIndex])
                higherIndex += 1
        
        # конец
        return newArr


print(merge_sort(genArray(150, 0, 1000)))
