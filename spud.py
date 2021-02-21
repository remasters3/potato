import time
import curses
from os import system
import movment as movment
import sonar as sonar
import lights as lights
import psounds as psounds
import time
#system('python movment.py')

## default and start settings
power = 100
agl = 90
pan = 90
movment.servoa(agl)
movment.servob (pan)
trigist = 40

try:
    while True:
        ## system('clear')
        frontdist = sonar.pingFront()
        reardist = sonar.pingRear()
        leftdist = sonar.pingLeft()
        rightdist = sonar.pingRight()
            
        if frontdist < trigist:
            while frontdist < trigist:
                # movment.allstop(0)
                movment.backwards(0,power)
                time.sleep(0.2)
                frontdist = sonar.pingFront()
            
        elif reardist < trigist:
            while reardist < trigist:
                # movment.allstop(0)
                movment.forward(0,power)
                time.sleep(0.2)
                reardist = sonar.pingRear()

        elif rightdist < trigist:
            while rightdist < trigist:
                # movment.allstop(0)
                movment.TurnLeft(0,power)
                time.sleep(0.2)
                rightdist = sonar.pingRight()
            
        elif leftdist < trigist:
            while leftdist < trigist:
                # movment.allstop(0)
                movment.TurnRight(0,power)
                time.sleep(0.2)
                leftdist = sonar.pingLeft()

        time.sleep(0.2)
        movment.allstop(0)
        print("Front - {0}. Rear - {1}. Left - {2}. Right {3}".format(frontdist,reardist,leftdist,rightdist))

finally:
    movment.servoa (90)
    movment.servob (90)
    system('clear')
    movment.allstop(0)
    movment.clearmp()
