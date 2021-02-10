import time
import curses
from os import system
import movment as movment
import sonar as sonar
import lights as lights
#system('python movment.py')

## default and start settings
power = 100
agl = 90
pan = 90
movment.servoa(agl)
movment.servob (pan)

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

        elif char == ord('s'):
            system('clear')
            if agl > 78:
                agl = agl-12
                movment.servoa(agl)
                print (agl)

        elif char == ord('w'):
            system('clear')
            if agl < 126:
                agl = agl+12
                movment.servoa(agl)
                print (agl)

        elif char == ord('a'):
            system('clear')
            if pan < 180:
                pan = pan+30
                movment.servob(pan)
                print (pan)
                
        elif char == ord('d'):
            system('clear')
            if pan > 0:
                pan = pan-30
                movment.servob(pan)
                print (pan)

        elif char == ord('l'):
            system('clear')
            lights.frontlight()

        elif char == ord('L'):
            system('clear')
            lights.camlight()

        elif char ==ord('p'):
            system('clear')
            dist = sonar.pingFront()
            print dist

        elif char == curses.KEY_UP:
    	    movment.allstop(0)
    	    system('clear')
            print " ^ "
    	    movment.forward(0,power)

        elif char == curses.KEY_DOWN:
    	    movment.allstop(0)
            system('clear')
            print " v "
            movment.backwards(0,power)
 
        elif char == curses.KEY_RIGHT:
    	    movment.allstop(0)
            system('clear')
            print "  >"
            movment.TurnRight(0,power)

        elif char == curses.KEY_LEFT:
    	    movment.allstop(0)
            system('clear')
            print "<  "
            movment.TurnLeft(0,power)

        elif char == 10:
            system('clear')
            print " - "
            movment.allstop(0)

finally:
    movment.servoa (90)
    movment.servob (90)
    system('clear')
    movment.allstop(0)
    movment.clearmp()
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()