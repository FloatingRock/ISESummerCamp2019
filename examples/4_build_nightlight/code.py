# Import the RPi.GPIO library and refer to it as GPIO
import RPi.GPIO as GPIO

# Use the BOARD mode for pin numbering
GPIO.setmode(GPIO.BOARD)

# Define the ports for the light sensor and the LED
LIGHT = 16
LED = 12

# Set the LIGHT port as input and the LED as output
GPIO.setup(LIGHT, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:

	while True:
		# Keep running the following until CTRL-C pressed
		# TODO: Add your code to create a night light here
		pass

except KeyboardInterrupt:
	print("Bye bye")

# Clean up on exit
GPIO.cleanup()
