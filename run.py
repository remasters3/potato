import RPi.GPIO as IO
import time
import curses
import RPi.GPIO as lightio
from os import system

IO.setwarnings(False)

IO.setmode(IO.BCM)
IO.setup(17,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(20,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)
# IO.setup(27,IO.OUT)

rf = IO.PWM(17,100)
rb = IO.PWM(22,100)
lf = IO.PWM(23,100)
lb = IO.PWM(24,100)
sa = IO.PWM(20,50)
sb = IO.PWM(16,50)
# lo = IO.PWM(27,100)

rf.start(0)
rb.start(0)
lf.start(0)
lb.start(0)
sa.start(0)
sb.start(0)
# lo.start(0)
# spd = 100
# def frontlight(lo,spd):
# lo.ChangeDutyCycle(100)

lightio.setmode(lightio.BCM)
lightio.setwarnings(False)
lightio.setup(27,lightio.OUT)
lightio.setup(21,lightio.OUT)
lightio.output(27,lightio.LOW)
lightio.output(21,lightio.LOW)
sa.ChangeDutyCycle(0)
sb.ChangeDutyCycle(0)


def servoa (agl):
    sa.ChangeDutyCycle(2+(agl/18))
    time.sleep(0.2)
    sa.ChangeDutyCycle(0)
    print (agl)
    
def servob (pan):
    sb.ChangeDutyCycle(2+(pan/18))
    time.sleep(0.1)
    sb.ChangeDutyCycle(0)
    print (pan)
    
def frontlight():
    if lightio.input(27) == 1:
        lightio.output(27, 0)
    elif lightio.input(27) == 0:
        lightio.output(27, 1)

def camlight():
    if lightio.input(21) == 1:
        lightio.output(21, 0)
    elif lightio.input(21) == 0:
        lightio.output(21, 1)

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
    ## IO.cleanup() #only needed at teh end
    rf.start(0)
    rb.start(0)
    lf.start(0)
    lb.start(0)
    time.sleep(tf)
    #system('aplay /usr/share/sounds/alsa/Noise.wav')

def threesixty():
    TurnRight(10.1,100)
    #time.sleep(11)
    allstop(0)
	
def oneeighty():
    TurnRight(5.09,100)
    #time.sleep(5.5)
    allstop(0)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
power = 100
agl = 90
pan = 90
servoa(agl)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
                
            elif char == ord('l'):
                system('clear')
                print "Front Light"
                frontlight()

            elif char == ord('L'):
                system('clear')
                print "Camera Light "
                camlight()

            elif char == ord('e'):
                system('clear')
                agl = 90
                pan = 90
                servoa (agl)
                system('clear')
                servob (pan)

            elif char == ord('t'):
                system('clear')
                pdst = 7
                allstop(0)
                forward(pdst,power)
                allstop(0)
                servob(15)
                oneeighty()
                allstop(0)
                servob(90)
                forward(pdst,power)
                allstop(0)
                servob(15)
                oneeighty()
                servob(90)
                allstop(0)
                agl = 90
                pan = 90
                servoa (agl)
                system('clear')
                servob (pan)

            elif char == ord('a'):
                system('clear')
                if pan < 180:
                     pan = pan+30
                     servob(pan)

            elif char == ord('d'):
                system('clear')
                if pan > 0:
                    pan = pan-30
                    servob(pan)

            elif char == ord('w'):
                system('clear')
                if agl < 126:
                     agl = agl+12
                     servoa(agl)

            elif char == ord('s'):
                system('clear')
                if agl > 78:
                    agl = agl-12
                    servoa(agl)

            elif char == ord('O'):
		allstop(0)
                system('clear')
                print "Three Sixty"
                threesixty()

            elif char == ord('o'):
		allstop(0)
                system('clear')
                print "One Eighty"
                oneeighty()

            elif char == curses.KEY_UP:
		allstop(0)
                system('clear')
                print "Forwards"
                forward(0,power)

            elif char == curses.KEY_DOWN:
		allstop(0)
                system('clear')
                print "Backwards"
                backwards(0,power)

            elif char == curses.KEY_RIGHT:
		allstop(0)
                system('clear')
                print "Turn right"
                TurnRight(0,power)

            elif char == curses.KEY_LEFT:
		allstop(0)
                system('clear')
                print "Turn left"
                TurnLeft(0,power)

            elif char == 10:
                system('clear')
                print "stop"
                allstop(0)
                # system('aplay -q /usr/share/sounds/alsa/Noise.wav') 
             
finally:
    servoa (90)
    servob (90)
    allstop(0)
    sa.stop()
    IO.cleanup()
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
