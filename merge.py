import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 3
ECHO = 4
maxtime = 0.04

Ena = 17
In1A = 27
In2A = 22

#defining pin 
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1A, GPIO.OUT)
GPIO.setup(In2A, GPIO.OUT)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(In1A, False)
GPIO.output(In2A, True)

pwm = GPIO.PWM(Ena, 100)

pwm.start(0)

def forward():
    pwm.ChangeDutyCycle(20)
    GPIO.output(Ena, True)

def stop():
    pwm.stop()
    GPIO.output(Ena, False)

def distance():
    GPIO.output(TRIG, False)
    time.sleep(0.01)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    start_time = time.time()
    timeout = start_time + maxtime
    while GPIO.input(ECHO) == 0 and start_time < timeout:
        start_time = time.time()
        
    end_time = time.time()
    timeout = end_time + maxtime
    while GPIO.input(ECHO) == 1 and end_time < timeout:
        end_time = time.time()

    t = end_time - start_time
    dist = (t*34300)//2
    return dist

while True:
    forward()
    d = distance()
    print("dist: ", d)
    if d == 13:
        stop()
        time.sleep(1)
    
    