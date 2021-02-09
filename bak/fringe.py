import RPi.GPIO as IO
import time

IO.setwarnings(False)

IO.setmode(IO.BCM)
IO.setup(17,IO.OUT) #12
IO.setup(22,IO.OUT) #18
IO.setup(23,IO.OUT) #
IO.setup(24,IO.OUT) #

rf = IO.PWM(17,100)
rb = IO.PWM(22,100)
lf = IO.PWM(23,100)
lb = IO.PWM(24,100)

rf.start(0)
rb.start(0)
lf.start(0)
lb.start(0)

rf.ChangeDutyCycle(100)
time.sleep(1)
rf.stop()

rb.ChangeDutyCycle(100)
time.sleep(1)
rb.stop()
