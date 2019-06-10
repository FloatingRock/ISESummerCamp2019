# Import the LightSensor module from the gpiozero library
from gpiozero import LightSensor

# Select pin 12 as your POTENTIOMETER pin
POTENTIOMETER = LightSensor(18)

try:

	while True:
		# Keep running the following until CTRL-C pressed
		print(POTENTIOMETER.value)

except KeyboardInterrupt:
	print("Bye bye")
