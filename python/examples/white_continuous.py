# TURN LEDS ON script for 3D Printer Case Project
#
# Author: Hervé PERCHEC <herve.perchec@gmail.com>
#
# Script based on the work of Tony DiCola (tony@tonydicola.com)
# 'NeoPixel library example'

import time

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

	print ('Press Ctrl-C to quit.')

	print ('Pixels : ' + str(strip.numPixels()))

	print ('Ultraviolet')
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, Color(0, 100, 255, 0)) # WARNING : GRBW format

	strip.show()

	for i in range(255):
		strip.setBrightness(i)
		strip.show()
		time.sleep(0.025)

#	for i in range(strip.numPixels()):
#		strip.setPixelColor(i, Color(0, 0, 0, 0))

#	strip.show()

#	while True:
#
#		for i in range(strip.numPixels()):
#			strip.setPixelColor(i, Color(255, 255, 255, 255))
#			strip.show()
#			time.sleep(0.05)
#			strip.setPixelColor(i, Color(0, 0, 0, 0))
#			strip.show()
#			time.sleep(0.05)

#		# 'Flash' loop
#		for i in range(10):
#			for i in range(strip.numPixels()):
#				strip.setPixelColor(i, Color(0, 100, 255, 0)) # 'Ultraviolet'
#
#			strip.show()
#
#			time.sleep(0.2)
#
#			for i in range(strip.numPixels()):
#                               strip.setPixelColor(i, Color(0, 0, 0, 0))
#
#			strip.show()
#
#			time.sleep(0.2)


#		# 'Police' loop
#		for i in range(15):
#			# For each pixel
#                        for j in range(strip.numPixels()):
#				# To alternate
#				if i%2 != 0:
#					# Left side from 1 to 16, the right from 17 to 32
#					if j < 17 : 
#						strip.setPixelColor(j, Color(0, 255, 0, 0)) # Red
#					else:
#						strip.setPixelColor(j, Color(0, 0, 255, 0)) # Blue
#				else:
#					if j < 17 :
#                                                strip.setPixelColor(j, Color(0, 0, 255, 0)) # Blue
#                                        else:
#                                                strip.setPixelColor(j, Color(0, 255,0, 0)) # Red
#			# Apply
#                        strip.show()
#			# Wait
#                        time.sleep(0.4)
#
#			# Turn off all the lights
#                        for i in range(strip.numPixels()):
#                                strip.setPixelColor(i, Color(0, 0, 0, 0))
#                        strip.show()
#                        time.sleep(0.2)
