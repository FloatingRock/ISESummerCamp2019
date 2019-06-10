# Import the RPi.GPIO library and refer to it as GPIO
import RPi.GPIO as GPIO

# Use the BOARD mode for pin numbering
GPIO.setmode(GPIO.BOARD)

# Select pin 12 as your LIGHT pin
LIGHT = 12

# Set the LIGHT port as input
GPIO.setup(LIGHT, GPIO.IN)

try:

	while True:
		# Keep running the following until CTRL-C pressed
		value = GPIO.input(LIGHT)
		print(value)

except KeyboardInterrupt:
	print("Bye bye")

# Clean up on exit
GPIO.cleanup()
