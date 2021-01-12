import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
servo = 17
GPIO.setup(servo, GPIO.OUT)
servo1 = GPIO.PWM(servo, 50)

servo1.start(0)



print("Rotating 180 degrees in 10 steps")

duty = 2

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1
    
time.sleep(2)

print("Going back to 90 degrees")
servo1.ChangeDutyCycle(7)

time.sleep(2)

print("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

servo1.stop()
GPIO.cleanup()