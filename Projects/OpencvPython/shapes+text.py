import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) #Size of matrix, three channels for color

#This is for is you only want to color a specific portion on the image
#img[200:300, 100:300] = 255, 0, 0 #Height, width

cv2.line(img, (0,0), (300, 300), (0,255,0), 3) #line(the image, (start point), (end poijnt), (color), thickness)

cv2.line(img, (512, 0), (0, img.shape[0]), (255, 0, 0), 3) #Can use img dimensions. So img.shape[0] is the images height, img.shape[1] is the width

cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2) #rectangle(the image, (upper left corner), (bottom right corner), color, thickness/cv2.FILLED)

cv2.circle(img, (400, 50), 30, (255, 255, 0), 5) #circle(the image, (center point), (radius), (color), thickness/cv2.FILLED)

cv2.putText(img, " OPENCV ", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2) #putText(the image, text, center point, font, scale, color, thickness)

cv2.imshow("Image", img)

cv2.waitKey(0)