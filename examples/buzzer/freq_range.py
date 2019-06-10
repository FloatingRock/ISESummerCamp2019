#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

BUZZ = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZ, GPIO.OUT)

try:
	while 1:
		for freq in range(100, 80000, 100):
			print(str(freq) + "Hz: " + str(2.0/freq))
			for i in range(0,freq/200):
				GPIO.output(BUZZ, 0)
				time.sleep(2.0/freq)
				GPIO.output(BUZZ, 1)
				time.sleep(2.0/freq)
except KeyboardInterrupt:
	pass

GPIO.cleanup()
