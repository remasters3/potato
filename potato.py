import RPi.GPIO as IO
import time
import curses
import RPi.GPIO as lightio
from os import system

IO.setwarnings(False)

IO.setmode(IO.BCM)
IO.setup(17,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)


rf = IO.PWM(17,100)
rb = IO.PWM(22,100)
lf = IO.PWM(23,100)
lb = IO.PWM(24,100)


rf.start(0)
rb.start(0)
lf.start(0)
lb.start(0)


lightio.setmode(lightio.BCM)
lightio.setwarnings(False)
lightio.setup(27,lightio.OUT)
lightio.output(27,lightio.LOW)

def lighton():
    lightio.output(27,lightio.HIGH)

def lightoff():
    lightio.output(27,lightio.LOW)

def forward(tf,spd):
    rf.ChangeDutyCycle(spd)
    lf.ChangeDutyCycle(spd)


def backwards(tf,spd):
    rb.ChangeDutyCycle(spd)
    lb.ChangeDutyCycle(spd)


def TurnRight(tf,spd):
    rb.ChangeDutyCycle(spd)
    lf.ChangeDutyCycle(spd)

    
def TurnLeft(tf,spd):
    lb.ChangeDutyCycle(spd)
    rf.ChangeDutyCycle(spd)


def allstop(tf):
    rf.stop()
    lf.stop()
    rb.stop()
    lb.stop()
    rf.start(0)
    rb.start(0)
    lf.start(0)
    lb.start(0)

def threesixty():
    TurnRight(8,100)
    time.sleep(15)
    allstop(0)
	
def oneeighty():
    TurnRight(8,100)
    time.sleep(7.5)
    allstop(0)

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
power = 100

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == ord('l'):
                system('clear')
                print "Lights on"
                lighton()
            elif char == ord('L'):
                system('clear')
                print "Lights off"
                lightoff()
            elif char == ord('p'):
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
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
