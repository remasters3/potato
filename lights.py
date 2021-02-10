import RPi.GPIO as lightio

lightio.setmode(lightio.BCM)
lightio.setwarnings(False)
lightio.setup(27,lightio.OUT)
lightio.setup(21,lightio.OUT)
lightio.output(27,lightio.LOW)
lightio.output(21,lightio.LOW)


def frontlight():
    if lightio.input(27) == 1:
        lightio.output(27, 0)
        print "Front Light off"
    elif lightio.input(27) == 0:
        lightio.output(27, 1)
        print "Front Light on"

def camlight():
    if lightio.input(21) == 1:
        lightio.output(21, 0)
        print "Camera Light off"
    elif lightio.input(21) == 0:
        lightio.output(21, 1)
        print "Camera Light on"