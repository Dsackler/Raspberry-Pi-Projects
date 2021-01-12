import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
delayt = 0.1
value = 0
ldr = 22
led = 27
servo = 17
GPIO.setup(servo, GPIO.OUT)
servo1 = GPIO.PWM(servo, 50)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,False)


def setup():
    servo1.start(0)


def rc_time(ldr):
    count = 0

    GPIO.setup(ldr,GPIO.OUT)
    GPIO.output(ldr,False)
    time.sleep(delayt)

    GPIO.setup(ldr,GPIO.IN)
    
    while(GPIO.input(ldr) == 0):
        count += 1
    return count

def destroy():
    servo1.stop()
    GPIO.cleanup()
    
def loop():
    Duty = 2
    while True:
        print("LDR Value: ")
        value = rc_time(ldr)
        print(value)
        if(value < 20000):
            print("lights are on")
            servo1.ChangeDutyCycle(2)
            time.sleep(0.1)
            #Duty = 7
            servo1.ChangeDutyCycle(0)
            time.sleep(0.1)
            GPIO.output(led,True)
        if(value >= 20000):
            print("Going 7")
            servo1.ChangeDutyCycle(7)
            time.sleep(0.2)
            print("Going 2")
            servo1.ChangeDutyCycle(2)
            time.sleep(0.2)
            #Duty = 7
            servo1.ChangeDutyCycle(0)
            time.sleep(0.2)
            GPIO.output(led,False)
    

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInturrupt:
        pass
    finally:
        destroy()
