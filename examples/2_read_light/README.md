# Example 2: Read Light Sensor

## Objective

Read the voltage from a light sensor and report the value.

## Circuit Diagram

![Image of circuit diagram](schem.png)

## Hardware Setup

![Image of hardware setup](bb.png)

## Software (`code.py`)

``` python
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
```

## Output

``` bash
$ python code.py
240
248
250
256
262
264
591
592
591
591
```

## Exploration

* The value gets larger when the sensor gets more light. Change the circuit to cause the value to become smaller as the sensor gets more light.
