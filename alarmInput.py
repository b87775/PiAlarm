import os
import datetime
import time
import pifacedigitalio as GPIO
GPIO = GPIO.PiFaceDigital()

prev_input = 0

while True:
	input = GPIO.switches[0].value
	GPIO.leds[2].turn_on()
	if ((not prev_input) and input):
		print("Button pressed")
		GPIO.leds[4].turn_on()
		os.system('/home/pi/home/theEmail.sh')
	prev_input = input
	GPIO.leds[4].turn_off()
	
	time.sleep(0.05)
