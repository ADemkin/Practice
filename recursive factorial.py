#!/usr/bin/env python3
#coding: utf-8
#
# факториал это перемножение всех чисел от 1 до данного.



def factorial_recursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        number = number * factorial_recursive(number - 1)
    return number

for i in range(0,25):
    print("Factorial of %d is %d" % (i, factorial_recursive(i)))




def main():
    pass


if __name__ == "__main__":
    main()
