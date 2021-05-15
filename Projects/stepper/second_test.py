import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ControlPin = [12, 16, 18, 22]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    
    
seq1 = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]

seq = [[1,0,0,1],
       [0,0,0,1],
       [0,0,1,1],
       [0,0,1,0],
       [0,1,1,0],
       [0,1,0,0],
       [1,1,0,0],
       [1,0,0,0]]

#512 for 1 revolution
#2560 for 5 revolutions
#5120 for 10 revolutions
#10240 for 20 revolutions


for i in range(10240):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep][pin])
        time.sleep(0.001)
        
#time.sleep(3)
        
GPIO.cleanup()

