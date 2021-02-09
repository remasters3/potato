import RPi.GPIO as IO
import time
import curses
from os import system

IO.setwarnings(False)

IO.setmode(IO.BCM)
IO.setup(17,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)
# IO.setup(27,IO.OUT)

rf = IO.PWM(17,100)
rb = IO.PWM(22,100)
lf = IO.PWM(23,100)
lb = IO.PWM(24,100)
# lo = IO.PWM(27,100)

rf.start(0)
rb.start(0)
lf.start(0)
lb.start(0)
# lo.start(0)
# spd = 100
# def lighton(lo,spd):
#    lo.ChangeDutyCycle(100)

def forward(tf,spd):
    rf.ChangeDutyCycle(spd)
    lf.ChangeDutyCycle(spd)
    # time.sleep(tf)

def backwards(tf,spd):
    rb.ChangeDutyCycle(spd)
    lb.ChangeDutyCycle(spd)
    # time.sleep(tf)

def TurnRight(tf,spd):
    rb.ChangeDutyCycle(spd)
    lf.ChangeDutyCycle(spd)
    # time.sleep(tf)
    
def TurnLeft(tf,spd):
    lb.ChangeDutyCycle(spd)
    rf.ChangeDutyCycle(spd)
    # time.sleep(tf)

def allstop(tf):
    rf.stop()
    lf.stop()
    rb.stop()
    lb.stop()
    # IO.cleanup() #only needed at teh end
    rf.start(0)
    rb.start(0)
    lf.start(0)
    lb.start(0)
    # time.sleep(tf)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
power = 100
# lighton(1,100)
try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
		allstop(0)
                system('clear')
                print "Forwards"
                forward(1,power)
            elif char == curses.KEY_DOWN:
		allstop(0)
                system('clear')
                print "Backwards"
                backwards(1,power)
            elif char == curses.KEY_RIGHT:
		allstop(0)
                system('clear')
                print "Turn right"
                TurnRight(1,power)
            elif char == curses.KEY_LEFT:
		allstop(0)
                system('clear')
                print "Turn left"
                TurnLeft(1,power)
            elif char == 10:
                system('clear')
                print "stop"
                allstop(0)   
             
finally:
    allstop(0)
    IO.cleanup()
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
