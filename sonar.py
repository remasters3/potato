import RPi.GPIO as SONAR
import time
SONAR.setmode(SONAR.BCM)

def pingFront():
    SONAR.setmode(SONAR.BCM)
    TRIG = 15
    ECHO = 14
    SONAR.setup(TRIG,SONAR.OUT)
    SONAR.output(TRIG,0)
    SONAR.setup(ECHO,SONAR.IN)
    time.sleep(0.1)

    SONAR.output(TRIG,1)
    time.sleep(0.00001)
    SONAR.output(TRIG,0)
    while SONAR.input(ECHO) == 0:
        pass
    start = time.time()
    while SONAR.input(ECHO) == 1:
        pass
    stop = time.time()

    dist = (stop - start) * 17000
    return float(dist)
    SONAR.cleanup()
