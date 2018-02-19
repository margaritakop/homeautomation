import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time # This is the time library, we need this so we can use the sleep function
import datetime

print 'Heya! I`m here to keep your plant alive.'
GPIO.setwarnings(False)
# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)
# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 17
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)
GPIO.setup(16, GPIO.OUT)

GPIO.output(16, False)

def gardening():
        while GPIO.input(channel):
                print "LED off, soil is dry!"
                pumping(2)
                logging_time()
                time.sleep(10)
        else:
                print "Plant is happy."

def pumping(secs):
        GPIO.output(16, True)
        print 'pumping water'
        time.sleep(secs)
        GPIO.output(16, False)
