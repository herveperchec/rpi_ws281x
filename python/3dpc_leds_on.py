# TURN LEDS ON script for 3D Printer Case Project
#
# Author: Herve PERCHEC (herve.perchec@gmail.com)
#
# Script based on the work of Tony DiCola (tony@tonydicola.com)
# 'NeoPixel library example'

import time
import json

from neopixel import *

# LED strip configuration:
LED_COUNT      = 32      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 0       # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	consoleResponse = {
		'script': '3dpc_leds_on.py',
		'data': {
			'pixels': strip.numPixels(), 
			'colorName': 'Ultraviolet',
			'colorGRBW': '(0, 100, 255, 0)',
			'status': 'on'
		}
	}

	# Format response to JSON
	print(json.dumps(consoleResponse, indent=4))

	for i in range(strip.numPixels()):
			strip.setPixelColor(i, Color(0, 100, 255, 0)) # WARNING : GRBW format

	strip.show()

	for i in range(255):
		strip.setBrightness(i)
		strip.show()
		time.sleep(0.025)

exit()