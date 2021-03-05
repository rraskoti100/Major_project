import RPi.GPIO as GPIO
import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)
GPIO.stemode(GPIO.BCM)
GPIO.setwarnings(False)

#pin configuration for motor driver
Ena = 17
In1A = 27
In2A = 22
#pin configuration for top servo
top_servo = 3
#pin configration for bottom servo
bottom_servo = 4
#pin configuration fot ultrasoic sensor
TRIG = 23
ECHO = 24

#defining pin as input and output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(top_servo, GPIO.OUT)
GPIO.setup(bottom_servo, GPIO.OUT)


GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1A, GPIO.OUT)
GPIO.setup(In2A, GPIO.OUT)

bottom_servo_pwm = GPIO.PWM(bottom_servo, 50)
top_servo_pwm = GPIO.PWM(top_servo, 50)
dc_pwm = GPIO.PWM(Ena, 100) # 100 is frequency

GPIO.output(In1A, True)
GPIO.output(In2A, False)
dc_pwm = start(0)

#required functions

def forward():
    dc_pwm.ChangeDutyCycle(20)
    GPIO.output(ENA, True)
    
def stop():
    dc_pwm.stop()
    GPIO.output(ENA, False)
    
def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    start_time = time.time()
    end_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()
        
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    t = end_time - start_time
    dist = (t*34300)//2
    return dist

def get_color():
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

    #time.sleep(1)
    #print("red : ", red)
    ##time.sleep(1)
    #print("Blue : ", blue)
    #time.sleep(1)
    #print("Green : ", green)
    #time.sleep(1)

    if red >= 200 & green <= 20 & blue <= 20:
        return "red"
    
    elif red <= 20 & green >= 200 & blue <= 20:
        return "green"
    
    else:
        return "invalid"
    
while True:
    


    












