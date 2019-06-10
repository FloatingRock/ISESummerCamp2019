import RPi.GPIO as GPIO
import time

BUZZ = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZ, GPIO.OUT)

p = GPIO.PWM(BUZZ, 1)
p.start(50)

try:

	for freq in range(50, 2000, 50):
		print(str(freq) + " " + 1/freq)
		p.ChangeFrequency(freq)
		time.sleep(1)

except KeyboardInterrupt:
	print("Bye bye")

# Clean up on exit
p.stop()
GPIO.cleanup()
