import time
from os import system
import movment as movment
import sonar as sonar
import time

power = 100
agl = 90
pan = 90
movment.servoa(agl)
movment.servob (pan)
maxdist = 200
mindist = 30

try:
    while True:
        fdist = sonar.pingFront()
        bdist = sonar.pingRear()
        ldist = sonar.pingLeft()
        rdist = sonar.pingRight()
        
        if ldist > rdist and ldist > fdist and ldist > bdist and ldist > mindist and ldist < maxdist:
            while ldist > rdist and ldist > fdist and ldist > bdist and ldist > mindist and ldist < maxdist:
                movment.TurnRight(0,power)
                fdist = sonar.pingFront()
                bdist = sonar.pingRear()
                ldist = sonar.pingLeft()
                rdist = sonar.pingRight()
                time.sleep(0.2)
                
        elif rdist > ldist and rdist > fdist and rdist > bdist and rdist > mindist and rdist < maxdist:
            while rdist > ldist and rdist > fdist and rdist > bdist and rdist > mindist and rdist < maxdist:
                movment.TurnLeft(0,power)
                fdist = sonar.pingFront()
                bdist = sonar.pingRear()
                ldist = sonar.pingLeft()
                rdist = sonar.pingRight()
                time.sleep(0.2)
                
        elif fdist > ldist and fdist > rdist and fdist > bdist and fdist > mindist and fdist < maxdist:
            while fdist > ldist and fdist > rdist and fdist > bdist and fdist > mindist and fdist < maxdist:
                movment.forward(0,power)
                fdist = sonar.pingFront()
                bdist = sonar.pingRear()
                ldist = sonar.pingLeft()
                rdist = sonar.pingRight()
                time.sleep(0.2)
                
        elif bdist > ldist and bdist > rdist and bdist > fdist and bdist > mindist and bdist < maxdist:
            while bdist > ldist and bdist > rdist and bdist > fdist and bdist > mindist and bdist < maxdist:
                movment.backwards(0,power)
                fdist = sonar.pingFront()
                bdist = sonar.pingRear()
                ldist = sonar.pingLeft()
                rdist = sonar.pingRight()
                time.sleep(0.2)
        else:
            movment.allstop(0)
        system('clear')
        print(" | Front:{0} | Rear:{1} | Left:{2} | Right:{3} |".format(fdist,bdist,ldist,rdist))
        time.sleep(0.2)
finally:
    movment.servoa (90)
    movment.servob (90)
    system('clear')
    movment.allstop(0)
    movment.clearmp()
