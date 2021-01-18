import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

my_colors = [[58, 171, 24, 89, 255, 54], #green
             [55, 201, 75, 179, 255, 178], #blue
             [31, 55, 54, 87, 153, 151]] #yellow

color_values = [[0, 153, 0],             #in BGR
                [255, 128, 0],
                [0, 255, 255]]

my_points = [] # [x, y, colorID]


def color_picker(img, my_colors, color_values):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points = []
    for color in my_colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(img_result, (x, y), 10, color_values[count], cv2.FILLED)
        if x != 0 and y != 0:
            new_points.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return new_points

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #(image, retrives extreme outer contours, amount of contour info to show)
    x ,y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(img_result, cnt, -1, (255,0,0), 3) #(image, contour, index(in this case -1 because we want all of them), color, thickness)
        perimeter = cv2.arcLength(cnt, True) #(contour, closed)
        corner_points = cv2.approxPolyDP(cnt, 0.02*perimeter, True) #(contour, resolution, closed)
        x, y, w, h = cv2.boundingRect(corner_points)
    return x+w//2,y

def draw_on_canvas(my_points, color_values):
    for point in my_points:
        cv2.circle(img_result, (point[0], point[1]), 10, color_values[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
    img_result = img_rotate_180.copy()
    new_points = color_picker(img_rotate_180, my_colors, color_values)
    if len(new_points) != 0:
        for newP in new_points:
            my_points.append(newP)
    if len(my_points) != 0:
        draw_on_canvas(my_points, color_values)
    cv2.imshow("Vid", img_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break