import cv2

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4) #(image, scale factor, minimum neighbors)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 2) #(img, initial points, corner points, color, thickness)


cv2.imshow('result', img)
cv2.waitKey(0)