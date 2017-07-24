#!/usr/bin/env python3
#coding: utf-8
#


from random import randint as rd


list = [[rd(0,100) for i in range(5)] for j in range(7)]

print(list)

for i in list:
    print(i)
    print(max(i[3]))







def main():
    pass


if __name__ == "__main__":
    main()
