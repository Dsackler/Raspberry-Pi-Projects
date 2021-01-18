import cv2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
servo = 17
GPIO.setup(servo, GPIO.OUT)
servo1 = GPIO.PWM(servo, 50)
servo1.start(0)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)



while True:
    duty = 1
    servo1.ChangeDutyCycle(0)
    success, img = cap.read()
    img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
    imgGray = cv2.cvtColor(img_rotate_180 , cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img_rotate_180 , (x, y), (x + w, y + h), (255, 0, 0), 2)
        rect = cv2.rectangle(img_rotate_180 , (x, y), (x + w, y + h), (255, 0, 0), 2)
        print(x)

        while x < 100 or x > 260:
            if x < 100:
                servo1.ChangeDutyCycle(duty + 1)
                duty = duty + 1
                time.sleep(0.1)
                servo1.ChangeDutyCycle(0)
            if x > 260:
                servo1.ChangeDutyCycle(duty - 1)
                duty = duty - 1
                time.sleep(0.1)
                servo1.ChangeDutyCycle(0)
    cv2.imshow('result', img_rotate_180)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        servo1.stop()
        GPIO.cleanup()
        break