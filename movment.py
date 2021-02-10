import RPi.GPIO as MP
import time
from os import system
MP.setwarnings(False)

MP.setmode(MP.BCM)

## main drive motors
MP.setup(17,MP.OUT)
MP.setup(22,MP.OUT)
MP.setup(23,MP.OUT)
MP.setup(24,MP.OUT)
rf = MP.PWM(17,100)
rb = MP.PWM(22,100)
lf = MP.PWM(23,100)
lb = MP.PWM(24,100)
rf.start(0)
rb.start(0)
lf.start(0)
lb.start(0)

## camera servos
MP.setup(16,MP.OUT)
MP.setup(20,MP.OUT)
sa = MP.PWM(20,50)
sb = MP.PWM(16,50)
sa.start(0)
sb.start(0)

def servoa (agl):
    sa.ChangeDutyCycle(2+(agl/18))
    time.sleep(0.2)
    sa.ChangeDutyCycle(0)
    
def servob (pan):
    sb.ChangeDutyCycle(2+(pan/18))
    time.sleep(0.1)
    sb.ChangeDutyCycle(0)

def forward(tf,spd):
    rf.ChangeDutyCycle(spd)
    lf.ChangeDutyCycle(spd)
    time.sleep(tf)
    # system('aplay -q /usr/share/sounds/alsa/Front_Center.wav')

def backwards(tf,spd):
    rb.ChangeDutyCycle(spd)
    lb.ChangeDutyCycle(spd)
    time.sleep(tf)
    # system('aplay -q /usr/share/sounds/alsa/Rear_Center.wav')

def TurnRight(tf,spd):
    rb.ChangeDutyCycle(spd)
    lf.ChangeDutyCycle(spd)
    time.sleep(tf)
    # system('aplay -q /usr/share/sounds/alsa/Front_Right.wav')
    
def TurnLeft(tf,spd):
    lb.ChangeDutyCycle(spd)
    rf.ChangeDutyCycle(spd)
    time.sleep(tf)
    # system('aplay -q /usr/share/sounds/alsa/Front_Left.wav')

def allstop(tf):
    rf.stop()
    lf.stop()
    rb.stop()
    lb.stop()
    rf.start(0)
    rb.start(0)
    lf.start(0)
    lb.start(0)
    time.sleep(tf)
    #system('aplay /usr/share/sounds/alsa/Noise.wav')

def threesixty():
    TurnRight(10.1,100)
    allstop(0)
	
def oneeighty():
    TurnRight(5.09,100)
    allstop(0)
	
def clearmp():
    sa.stop()
    sb.stop()
    MP.cleanup()