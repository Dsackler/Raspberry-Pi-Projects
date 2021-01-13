import cv2
print("Imported")


# img = cv2.imread("Resources/Danielle.jpeg")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# cv2.imshow("Dani", img)
# cv2.waitKey(0)

while True:
    success, img = cap.read()
    cv2.imshow("Vid", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break