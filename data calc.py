# coding: utf-8
'''
Этот скрипт спрашивает у пользователя количество дней и
высчитывает дату, которая наступит через количество дней,
введенных пользователем
'''

import datetime


def main():
    r = int(input('Enter how many days to go: '))
    delta = datetime.timedelta(days=+r)
    today = datetime.datetime.now()
    d = today + delta
    print('%d days from today will be %d.%d.%d' % (r, d.day, d.month, d.year))


if __name__ == "__main__":
    main()
