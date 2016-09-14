import time
import datetime
import random

today = time.strftime("%d/%m/%y", time.gmtime()) 
now = time.strftime("%H:%M:%S", time.gmtime()) 

print "It's %s, on %s." % (now, today)
print "Pick a date in the future."
yearfut = input("Pick a year: ")
monthfut = input("Pick a month: ")
dayfut = input("Pick a day in that month: ")

futdate = datetime.time(yearfut, monthfut, dayfut)
print futdate

diff = futdate - today
print diff

print "Your date, %s, is %s in the future." % (futdate, diff)
