#get you RPi to wake you up to the curtain being drawn (or anything else hooked to GPIO 8)

import RPi.GPIO as GPIO
import time
import datetime
from random_words import RandomWords

alarm = input("What time would you like to wake up? ")
structTime = time.localtime()
now = datetime.datetime(*structTime[:6])

now = str(now)[11:16]
print ("Alarm is set for " + alarm + ". The time now is " + now + ".")

rw = RandomWords()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

draw = 10 #time for duration of the curtain draw

while True:
    structTime = time.localtime()
    current1 = datetime.datetime(*structTime[:6])
    current2 = str(current1)[11:16]
    GPIO.output(8, False)
    word1 = rw.random_word()
    word2 = rw.random_word()
    print ("Sleep well Mara! Dream of " + word1 + " and " + word2)
    time.sleep(30)
