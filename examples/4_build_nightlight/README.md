# Example 4: Build a Nightlight

## Objective

Create a nightlight by linking the value of the light sensor to the LED output. Determine a threshold for the light sensor and enable the LED when the room is dark; and disable the LED when the room has adequate light. Additionally, print the word "DAY" on the terminal one time on the transition to day and the word "NIGHT" one time on the transition to night.

In this example, the provided code is just a skeleton for the final solution. This will provide you with an opportunity to create a custom solution.
Read the voltage from a potentiometer and report the value.

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
```

## Output

``` bash
$ python code.py
DAY
NIGHT
DAY
NIGHT
DAY
NIGHT
DAY
```
