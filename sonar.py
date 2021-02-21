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
    return int(dist)
    SONAR.cleanup()
    
def pingRear():
    SONAR.setmode(SONAR.BCM)
    TRIG = 19
    ECHO = 26
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
    return int(dist)
    SONAR.cleanup()

def pingLeft():
    SONAR.setmode(SONAR.BCM)
    TRIG = 6
    ECHO = 13
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
    return int(dist)
    SONAR.cleanup()

def pingRight():
    SONAR.setmode(SONAR.BCM)
    TRIG = 21
    ECHO = 12
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
    return int(dist)
    SONAR.cleanup()