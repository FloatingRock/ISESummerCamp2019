# Import the RPi.GPIO library and refer to it as GPIO
import RPi.GPIO as GPIO
import time

# Use the BOARD mode for pin numbering
GPIO.setmode(GPIO.BOARD)

# Select pin 12 as your LED pin
LED = 12

# Set the LED port as output and assign it an initial value
GPIO.setup(LED, GPIO.OUT)

try:

	while True:
		# Keep running the following until CTRL-C pressed
		GPIO.output(LED, 1)
		print("LED ON")
		time.sleep(0.5)
		GPIO.output(LED, 0)
		print("LED OFF")
		time.sleep(0.5)

except KeyboardInterrupt:
	print("Bye bye")

# Clean up on exit
GPIO.cleanup()
