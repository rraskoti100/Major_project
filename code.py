import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #cv2.imshow("frame", frame)

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # red color mask creation
    upper_red1 = np.array([20, 255, 255])
    lower_red1 = np.array([0, 50, 50])
    mask1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
    upper_red2 = np.array([179, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    mask2 = cv2.inRange(img_hsv, lower_red2, upper_red2)
    mask_red = mask1 + mask2
    count_red = cv2.countNonZero(mask_red)

    # blue color mask creation
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([130, 255, 255])
    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
    count_blue = cv2.countNonZero(mask_blue)

    # mask creation for green color
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])
    mask_green = cv2.inRange(img_hsv, lower_green, upper_green)
    count_green = cv2.countNonZero(mask_green)

    # mask creation for white color
    lower_white = np.array([0, 42, 0])
    upper_white = np.array([179, 255, 255])
    mask_white = cv2.inRange(img_hsv, lower_white, upper_white)
    op_img = cv2.bitwise_and(frame, frame, mask = mask_white)

    cv2.imshow("Colors", op_img)

    red = mask_red.sum()//100000
    green = mask_green.sum()//100000
    blue = mask_blue.sum()//100000

    time.sleep(1)
    print("red : ", red)
    time.sleep(1)
    print("Blue : ", blue)
    time.sleep(1)
    print("Green : ", green)
    time.sleep(1)

    if red >= 250 and green <= 5 and blue <= 5:
        print("RED color")
        time.sleep(1)
    if red <= 5 and green >= 250 and blue <= 5:
        print("GREEN  color")
        time.sleep(1)
    else:
        print("Color not detected.")
        time.sleep(1)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()