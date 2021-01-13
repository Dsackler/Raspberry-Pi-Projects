import cv2

img = cv2.imread("Resources/Danielle.jpeg")

print(img.shape)

imgResize = cv2.resize(img,(1000, 500)) #(Width, Height)
imgCropped = img[0:200, 200:500] #height, width

cv2.imshow("Original", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)