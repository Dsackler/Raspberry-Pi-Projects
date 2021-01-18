import cv2

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)



while True:
    success, img = cap.read()
    img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
    imgGray = cv2.cvtColor(img_rotate_180 , cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img_rotate_180 , (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('result', img_rotate_180)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break