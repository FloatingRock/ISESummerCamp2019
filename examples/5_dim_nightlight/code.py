from gpiozero import LED, LightSensor

LIGHT = LightSensor(16)
LED = LED(12)

try:

	while True:
		# Keep running the following until CTRL-C pressed
		# TODO: Add your code to create a night light here
		pass

except KeyboardInterrupt:
	print("Bye bye")
