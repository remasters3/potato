import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LED = 21
ledState = False
GPIO.setup(LED,GPIO.OUT)

ledState = ledState
GPIO.output(LED, ledState)
