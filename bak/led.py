import RPi.GPIO as lightio
import time
lightio.setmode(lightio.BCM)
lightio.setwarnings(False)
lightio.setup(27,lightio.OUT)
print "LED on"
lightio.output(27,lightio.HIGH)
time.sleep(10)
print "LED off"
lightio.output(27,lightio.LOW)
