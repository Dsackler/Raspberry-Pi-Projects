import RPi.GPIO as GPIO
import time

led = 20
pir = 27

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(pir, GPIO.IN)

def loop():
    while True:
        if GPIO.input(pir) == GPIO.HIGH:
            GPIO.output(led, GPIO.HIGH)
            print("LED on")
        else:
            GPIO.output(led, GPIO.LOW)
            print("LED off")

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInturrupt:
        pass
    finally:
        destroy()
    
    