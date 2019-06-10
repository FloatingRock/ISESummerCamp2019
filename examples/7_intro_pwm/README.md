# Example 7: Introduce Pulse-Width Modulation (PWM)

## Objective

This example builds on top of the previous one.
Get familiar with the PWM library of RPi.GPIO.

## Software (`code.py`)

The previous example provided code that generates sound waves of different frequencies `freq` for the buzzer:

``` python
for freq in range(50, 2000, 50):
  print(str(freq) + " " + 1/freq)
  for j in range(0, freq/5):
    GPIO.output(BUZZ, 0)
    time.sleep(2.0/freq)
    GPIO.output(BUZZ, 1)
    time.sleep(2.0/freq)
```

Here we manually switch between 0 (LOW) and 1 (HIGH) at a given frequency (50Hz = 50 times per second). This is also known as a square wave with a duty cycle of 50% (half the time the signal is HIGH, the other half of the time the signal is LOW). This type of information encoding is known as Pulse-Width Modulation (PWM).

![Image of PWM](pwm.gif)

We can use the PWM library of RPi.GPIO to change the code above to:

``` python
p = GPIO.PWM(BUZZ, 1)
p.start(50)

for freq in range(50, 2000, 50):
  print(str(freq) + " " + 1/freq)
  p.ChangeFrequency(freq)
  time.sleep(1)

p.stop()
```

Change the code from the previous example accordingly and observe the result. The output will be the same, but we simplified the code by a big margin.
