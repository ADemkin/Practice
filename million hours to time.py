#!/usr/bin/env python3
# coding: utf-8
#

import datetime

m = 10**6

zerotime = datetime.datetime(1, 1, 1, 0, 0)

time = datetime.timedelta(hours=m)

#print('One million hours is ' + (zerotime + time).strftime('%d.%m.%Y  %H:%M:%S'))

this_year = datetime.datetime.now().year
print(this_year)
bday = datetime.datetime(year=this_year ,month=9, day=14)

now = datetime.datetime.now()

time_until_bday = now - bday

print(str(abs(time_until_bday.days)) + " days until my birthday.")