import RPi.GPIO as IO
import time
import curses

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
#spd = 100

def forward(tf,spd):
    rf.ChangeDutyCycle(spd)
    lf.ChangeDutyCycle(spd)
    #time.sleep(tf)

def backwards(tf,spd):
    rb.ChangeDutyCycle(spd)
    lb.ChangeDutyCycle(spd)
    #time.sleep(tf)

def TurnRight(tf,spd):
    rb.ChangeDutyCycle(spd)
    lf.ChangeDutyCycle(spd)
    #time.sleep(tf)
    
def TurnLeft(tf,spd):
    lb.ChangeDutyCycle(spd)
    rf.ChangeDutyCycle(spd)
    #time.sleep(tf)

def allstop(tf):
    rf.stop()
    lf.stop()
    rb.stop()
    lb.stop()
    IO.cleanup()
    #time.sleep(tf)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                print "up"
                forward(1,70)
            elif char == curses.KEY_DOWN:
                print "down"
                backwards(1,70)
            elif char == curses.KEY_RIGHT:
                print "right"
                TurnRight(1,70)
            elif char == curses.KEY_LEFT:
                print "left"
                TurnLeft(1,70)
            elif char == 10:
                print "stop"
                allstop(tf)   
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
