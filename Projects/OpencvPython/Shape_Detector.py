import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #(image, retrives extreme outer contours, amount of contour info to show)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3) #(image, contour, index(in this case -1 because we want all of them), color, thickness)
            perimeter = cv2.arcLength(cnt, True) #(contour, closed)
            corner_points = cv2.approxPolyDP(cnt, 0.02*perimeter, True) #(contour, resolution, closed)
            amount_corners = len(corner_points)
            x, y, w, h = cv2.boundingRect(corner_points)

            if amount_corners == 3:
                objectType = 'Tri'
            elif amount_corners == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = 'Square'
                else:
                    objectType = 'Rectangle'
            else:
                objectType = 'Circle'

            cv2.rectangle(imgContour, (x,y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, (x + (w//2) - 10, y + (h//2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)

img = cv2.imread("Resources/Shapes.jpg")
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)


cv2.imshow("Original", img)
cv2.imshow("Contour", imgContour)
cv2.imshow("Canny", imgCanny)
cv2.waitKey(0)

