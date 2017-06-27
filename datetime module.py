#!/usr/bin/env python3
#coding: utf-8
#

import datetime


#print(help(datetime.time))

# my birthday date
bd = (datetime.date(1987, 9, 14))

print(bd)

# 6000 days
delta = datetime.timedelta(6000)

# add a date and a time delta
print(bd + delta)

# format a string differently
# russian date format
print(bd.strftime('%d.%m.%Y '))


