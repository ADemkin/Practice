# calcuates fibanacci number
# fibanacci_recursive number is a result of sum of two previous fibanacci_recursive numbers

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibanacci_recursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibanacci_recursive(number - 1) + fibanacci_recursive(number - 2)


def fibanacci_non_recursive(number):
    sequence = [0, 1]
    while len(sequence) < number:
        sequence.append(sequence[len(sequence) - 2] + sequence[len(sequence) - 1])
    return sequence


def golden_ratio():
    '''
    As we all know, every next fibanacci number is exactly 1.6 timers larger than previous one.
    Lets calculate that number precisely.
    '''
    accuracy = 42
    fib = fibanacci_non_recursive(accuracy)
    # for i in range(2, len(fib)):
    #     g = (fib[i] / fib[i - 1])
    #     print("%d\t %.50f" % (i, g))
    golden_ratio = fib[len(fib)-1] / fib[len(fib)-2]
    # print("%.50f" % (golden_ratio))
    return golden_ratio
    

def main():
    # print("Print first twenty fibanacci numbers using recursion:")
    # for num, i in enumerate(range(21)):
    #     print(num, '\t', fibanacci_recursive(i))
    # print("First twenty fibanacci numbers using while cycle:")
    # for num, i in enumerate(fibanacci_non_recursive(21)):
    #     print('%d \t %d' % (num, i))
    #print("%.50f" % golden_ratio())
    
    for i in range(1000):
        print( '%d\t%d' % (i, fibanacci_recursive(i)))


if __name__ == "__main__":
    main()
