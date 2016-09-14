import datetime
import time
from time import sleep

import os

i = 1

while i == 1:
	#print(time.perf_counter())
	print("Get some water mate!!!..")
	os.system('cvlc bell-ringing-01.mp3 &')
	sleep(1)
	os.system('pkill vlc')
