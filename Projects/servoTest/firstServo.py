import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)

servo1.start(0)

duty = 2

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1

time.sleep(1)


servo1.ChangeDutyCycle(7) #go to 90 degrees
time.sleep(0.5)
servo1.ChangeDutyCycle(0) #turn off to get rid of jitter

servo1.ChangeDutyCycle(2)
time.sleep(0.5)


servo1.stop()
GPIO.cleanup()

