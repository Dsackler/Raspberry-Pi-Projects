import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
btnPin = 36



def setup():
    GPIO.setup(btnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #GPIO.add_event_detect(btnPin, GPIO.FALLING, callback = servomov)
    servo1.start(0)
    servo1.ChangeDutyCycle(7)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)





def servomov():
    flap = True
    while True:
        input_state = GPIO.input(btnPin)
        
        if input_state == False and flap == True:
            flap = False
            print("btn")
            servo1.ChangeDutyCycle(2)
            time.sleep(0.3)
            servo1.ChangeDutyCycle(0)
    
        elif input_state == False and flap == False:
            flap = True
            print("btn 2")
            servo1.ChangeDutyCycle(7)
            time.sleep(0.3)
            servo1.ChangeDutyCycle(0)
            
        
def destroy():
    servo1.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        servomov()
    except KeyboardInterrupt:
        destroy()



