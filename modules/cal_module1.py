#calendar module

'''import calendar
year=2026
month=8
print(calendar.month(year,month))

import calendar
year=2027
print(calendar.calendar(year))

import calendar
year=int(input("enter a year"))
print(calendar.calendar(year))

import calendar
a=int(input("enter a year "))
b=int(input("enter the month "))
print(calendar.month(a,b))

#date and time

from datetime import date
a=date.today()
print(a)

import datetime
a=datetime.datetime.now()
print(a)

import time
a=time.time()
print(a)

b=time.localtime(a)
print(b)

#converting into human readable time

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"time is {b.tm_hour}h:{b.tm_min}m:{b.tm_sec}s")

print(f"today date and time is {b.tm_mday}-{b.tm_mon}-{b.tm_year}  {b.tm_hour}h:{b.tm_min}m:{b.tm_sec}s")

print(f"day is {b.tm_mday}-{b.tm_yday}-{b.tm_isdst}")

#task

import random
import time
for i in range(10):
    a=random.randint(10,20)
    print(a)
    time.sleep(2)

#error handling

#syntax error

for i in range(10):
print(i)

#run_time error

a=int(input())
b=int(input())
print(a//b)

#logical error

a=10
b=20
print(a-b)

a=10
b=20
if a<b:
    print("less")'''

a=10
b=20
if a>b:
    print("less")


