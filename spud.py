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

try:
    while True:
        system('clear')
        dist = sonar.pingFront()
        print ("{0}".format(dist))
            
        while dist < 30:
            movment.allstop(0)
            movment.TurnLeft(0,power)
            time.sleep(4)
            dist = sonar.pingFront()
            print ("{0}".format(dist))

        time.sleep(0.2)
        movment.allstop(0)
        movment.forward(0,power)

finally:
    movment.servoa (90)
    movment.servob (90)
    system('clear')
    movment.allstop(0)
    movment.clearmp()
