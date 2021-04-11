import RPi.GPIO as lightio

lightio.setmode(lightio.BCM)
lightio.setwarnings(False)
lightio.setup(10,lightio.OUT)
lightio.setup(9,lightio.OUT)
lightio.output(10,lightio.LOW)
lightio.output(9,lightio.LOW)

def frontlight():
    if lightio.input(10) == 1:
        lightio.output(10, 0)
        print ("Front Light off")
    elif lightio.input(10) == 0:
        lightio.output(10, 1)
        print ("Front Light on")

def camlight():
    if lightio.input(9) == 1:
        lightio.output(9, 0)
        print ("Camera Light off")
    elif lightio.input(9) == 0:
        lightio.output(9, 1)
        print ("Camera Light on")