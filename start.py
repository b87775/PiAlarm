import subprocess
import pifacedigitalio as GPIO
import time
import os

GPIO = GPIO.PiFaceDigital()

while True:
	if (GPIO.switches[0]):
		GPIO.leds[1].turn_on()
		os.system("sudo python3 /home/pi/home/alarmInput.py")
