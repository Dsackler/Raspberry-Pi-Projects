import cv2
import numpy as np

# img = cv2.imread("Resources/Danielle.jpeg")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)



# imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# cv2.imshow("Original", img)
# cv2.imshow("HSV", imgHSV)
# cv2.waitKey(0)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("Vid", imgHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break