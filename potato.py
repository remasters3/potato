import time
import curses
from os import system
import movment as movment
import sonar as sonar
#system('python movment.py')


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
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
    
        elif char == curses.KEY_UP:
    	    movment.allstop(0)
    	    system('clear')
    	    print "^"
    	    movment.forward(0,power)
            dist = sonar.ping()
            #print dist
    
        elif char == curses.KEY_DOWN:
    	    movment.allstop(0)
            system('clear')
            print "v"
            movment.backwards(0,power)
    
        elif char == curses.KEY_RIGHT:
    	    movment.allstop(0)
            system('clear')
            print ">"
            movment.TurnRight(0,power)
    
        elif char == curses.KEY_LEFT:
    	    movment.allstop(0)
            system('clear')
            print "<"
            movment.TurnLeft(0,power)
    
        elif char == 10:
            system('clear')
            print "stop"
            movment.allstop(0)
            # system('aplay -q /usr/share/sounds/alsa/Noise.wav') 
         
finally:
    movment.clearmp()
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
			
			