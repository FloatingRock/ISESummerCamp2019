# Example 8: Play a sound sequence

## Objective

Get familiar with writing and playing a sound sequence for the buzzer.

## Software (`code.py`)

So far we have produced sound waves with arbitrary frequencies. Next we will write code to play a well-known sound sequence.

A sound sequence consists of a series of musical notes with a given pitch and duration of a sound. The pitch is the frequency of the sound wave that we generate and the duration is the time during which we keep producing said sound wave.

Below is a list of some common musical pitches and durations:

``` python
notes = {'C' : 523.25, 'D' : 587.33, 'E' : 659.25, 'F' : 349.23, 'G' : 392.00, 'A' : 440.00, 'B' : 493.88, '#' : 0.5, 'Ab' : 415.30}
speed = {'sw' : 1, 'w' : 0.8, 'h' : 0.6 , 'q' : 0.45, 'qh' : 0.25, 'qhh' : 0.15}
```

Having such mappings set up makes it a lot easier to write a sound sequence either by ear or from a sheet music. Lets write two python functions for playing a given musical note and for simply pausing for a given duration:

``` python
def play(note, duration):
  p.ChangeFrequency(notes[note])
  p.ChangeDutyCycle(50)
  time.sleep(speed[duration])

def pause(duration):
  play('#', duration)
```

Note, that the `pause` function makes use of the `#` pitch, which was defined as a 1Hz frequency, which essentially translates to: play something that neither the buzzer can play nor the human ear can hear.

With all that setup, we can create a sound sequence, by simply concatenating a series of `play` function calls:

``` python
play('E', 'q')
play('B', 'qh')
play('C', 'qh')
play('D', 'q')
play('C', 'qh')
play('B', 'qh')
play('A', 'q')
```

Below is the full code:

``` python
#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

BUZZ = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZ, GPIO.OUT)

p = GPIO.PWM(BUZZ, 1)
p.start(50)

notes = {'C' : 523.25, 'D' : 587.33, 'E' : 659.25, 'F' : 349.23, 'G' : 392.00, 'A' : 440.00, 'B' : 493.88, '#' : 0.5, 'Ab' : 415.30}
speed = {'sw' : 1, 'w' : 0.8, 'h' : 0.6 , 'q' : 0.45, 'qh' : 0.25, 'qhh' : 0.15}

def play(note, duration):
  p.ChangeFrequency(notes[note])
  p.ChangeDutyCycle(50)
  time.sleep(speed[duration])

def pause(duration):
  play('#', duration)

try:

  play('E', 'q')
  play('B', 'qh')
  play('C', 'qh')
  play('D', 'q')
  play('C', 'qh')
  play('B', 'qh')
  play('A', 'q')

  # TODO: edit the sound sequence below
  play('A', 'qhh')
  play('C', 'qhh')
  play('E', 'qhh')
  play('D', 'qhh')
  play('C', 'qhh')
  play('B', 'qhh')
  play('C', 'qhh')
  play('D', 'qhh')
  play('E', 'qhh')
  play('C', 'qhh')
  play('A', 'qhh')
  play('A', 'qhh')

except KeyboardInterrupt:
        pass

p.stop()
GPIO.cleanup()
```

Play it and see if you recognize the tune. Notice, that the first 7 notes have the correct duration and that the remaining notes do not. It is left as an exercise for you to fix the remaining durations to complete this well-known tune.

## Exploration

This is your chance to use the provided framework code to either translate your favorite tune and play it on the buzzer or to write your own music.
