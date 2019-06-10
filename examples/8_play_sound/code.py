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
