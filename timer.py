from datetime import datetime
from datetime import timedelta
from time import sleep
from time import strptime
from time import strftime

class Timer(object):

    now = datetime.now()

    def __init__(self, timevalue):
        self.timevalue = timevalue

    def inputtime(self):
        return datetime.strptime(self.timevalue, "%H:%M:%S %d-%m-%Y")

    def printtime(self):
        print(self.timevalue)

    def countdown(self):
        diff = self.inputtime() - self.now
        return diff

    def timediff(self, value):
        diff = self.inputtime() - datetime.strptime(value, "%H:%M:%S %d-%m-%Y")
        return diff

    def delt(self,days,hours,mins,secs):
        timedelt = timedelta(days=days,hours=hours, minutes=mins, seconds=secs)
        diff = self.now + timedelt
        return diff

    def printcountdown(self):
        nowseconds = self.now.timestamp()
        endseconds = datetime.strptime(self.countdown(), "%H:%M:%S %d-%m-%Y").timestamp()
        cntdwn = abs(nowseconds-endseconds)
        return cntdwn



time1 = Timer("17:00:00 12-05-2017")

print(time1.delt(0,8.5,0,0))
print(time1.printcountdown())

'''

    def timediff(number):
        seconds = round(abs(time() - number)) % 60
        mins = str(((abs(time() - number)) / 60) % 60).split('.')[0]
        hours = str(((abs(time() - number)) / 3600)).split('.')[0]
        return {'s': seconds,'m': mins,'h': hours}

    def printdiff(tv):
        print("Seconds:", timediff(tv)['s'],
                "\tMins:", timediff(tv)['m'],
                "\tHours:", timediff(tv)['h'],
                end='\r', flush=True)

    def countdown(timevalue):
        return print(timediff(timevalue))
        
    countdown(100)
    '''
