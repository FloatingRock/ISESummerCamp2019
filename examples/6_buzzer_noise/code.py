import RPi.GPIO as GPIO
import time


BUZZ = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZ, GPIO.OUT)

try:

	for i in range(50, 2000, 50):
		print(str(i) + " " + 1/i)
		for j in range(0, i/5):
			GPIO.output(BUZZ, 0)
			time.sleep(2.0/i)
			GPIO.output(BUZZ, 1)
			time.sleep(2.0/i)

except KeyboardInterrupt:
	print("Bye bye")

# Clean up on exit
GPIO.cleanup()
