import time
import curses
from os import system
import movment as movment
import sonar as sonar
import lights as lights
import psounds as psounds

power = 100
agl = 90
pan = 90
movment.servoa(agl)
movment.servob (pan)

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
            if agl > 56:
                agl = agl-12
                movment.servoa(agl)
                print ("{0}".format(agl))

        elif char == ord('w'):
            system('clear')
            if agl < 138:
                agl = agl+12
                movment.servoa(agl)
                print ("{0}".format(agl))

        elif char == ord('a'):
            system('clear')
            if pan < 180:
                pan = pan+30
                movment.servob(pan)
                print ("{0}".format(pan))

        elif char == ord ('e'):
            system('clear')
            agl = 90
            pan = 90
            movment.servoa(agl)
            movment.servob(pan)
            
        elif char == ord('d'):
            system('clear')
            if pan > 0:
                pan = pan-30
                movment.servob(pan)
                print ("{0}".format(pan))
                
        elif char == ord('h'):
            system('clear')
            psounds.horn()
            print ("{0}".format("Beep! Beep!"))
            
        elif char == ord('f'):
            system('clear')
            psounds.shoot()
            print ("{0}".format("Fire in the hole!"))
            
        elif char == ord('b'):
            system('clear')
            psounds.bark()
            print ("{0}".format("Wuff!"))

        elif char == ord('g'):
            system('clear')
            psounds.hello()
            print ("{0}".format("Hallo"))            

        elif char == ord('G'):
            system('clear')
            psounds.bye()
            print ("{0}".format("ttfn"))

        elif char == ord('t'):
            system('clear')
            psounds.thanks()
            print ("{0}".format("danke!"))            

        elif char == ord('T'):
            system('clear')
            psounds.uwelcome()
            print ("{0}".format("You're Welcome!"))

        elif char == ord('y'):
            system('clear')
            psounds.yes()
            print ("{0}".format("Yes!"))            

        elif char == ord('Y'):
            system('clear')
            psounds.no()
            print ("{0}".format("No!"))

        elif char == ord('l'):
            system('clear')
            lights.frontlight()

        elif char == ord('L'):
            system('clear')
            lights.camlight()

        elif char ==ord('p'):
            system('clear')
            frontdist = sonar.pingFront()
            reardist = sonar.pingRear()
            leftdist = sonar.pingLeft()
            rightdist = sonar.pingRight()
            psounds.ping()
            print("| Front:{0} | Rear:{1} | Left:{2} | Right:{3} |".format(frontdist,reardist,leftdist,rightdist))

        elif char == curses.KEY_UP:
            movment.allstop(0)
            system('clear')
            dist = 31
            ## dist = sonar.pingFront()
            if dist > 30:
                print(' ^ ')
                movment.forward(0,power)
                psounds.move()
            else:
                print ("Obstruction Detected at {0}cm".format(dist)) 

        elif char == curses.KEY_DOWN:
            movment.allstop(0)
            system('clear')
            print(" v ")
            movment.backwards(0,power)
            psounds.move()
 
        elif char == curses.KEY_RIGHT:
            movment.allstop(0)
            system('clear')
            print("  >")
            movment.TurnRight(0,power)
            psounds.move()

        elif char == curses.KEY_LEFT:
            movment.allstop(0)
            system('clear')
            print("<  ")
            movment.TurnLeft(0,power)
            psounds.move()

        elif char == 10:
            system('clear')
            print(" - ")
            movment.allstop(0)
            psounds.stop()

finally:
    movment.servoa (90)
    movment.servob (90)
    system('clear')
    movment.allstop(0)
    movment.clearmp()

    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
