# Import the LightSensor module from the gpiozero library
from gpiozero import LightSensor

# Select pin 12 as your LIGHT pin
LIGHT = LightSensor(18)

try:

	while True:
		# Keep running the following until CTRL-C pressed
		print(LIGHT.value)

except KeyboardInterrupt:
	print("Bye bye")
