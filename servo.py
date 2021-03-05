import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

#mode setup for raspberry pi
GPIO.setmode(GPIO.BCM)

#pin setup for servo motor
top_servo = 4
bottom_servo = 3

GPIO.setup(top_servo, GPIO.OUT)
top_pwm = GPIO.PWM(top_servo, 50) # 50 is frequency

GPIO.setup(bottom_servo, GPIO.OUT)
bottom_pwm = GPIO.PWM(bottom_servo, 50)

top_pwm.start(0)
bottom_pwm.start(0)

while True:
    #position 1
    bottom_pwm.ChangeDutyCycle(10)
    sleep(1)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.4)

    #position 2
    bottom_pwm.ChangeDutyCycle(8)
    sleep(1)
    top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
    #position 1
    bottom_pwm.ChangeDutyCycle(10)
    sleep(1)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
    #position 3
    bottom_pwm.ChangeDutyCycle(6)
    sleep(1)
    top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
    #position 1
    bottom_pwm.ChangeDutyCycle(10)
    sleep(1)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
    
    #position 4
    bottom_pwm.ChangeDutyCycle(4)
    sleep(1)
    top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
    #position 1
    bottom_pwm.ChangeDutyCycle(10)
    sleep(1)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.4)
    
    #position 5
    bottom_pwm.ChangeDutyCycle(2)
    sleep(1)
    top_pwm.ChangeDutyCycle(5)
    sleep(0.5)
    top_pwm.ChangeDutyCycle(15)
    sleep(0.4)  

top_pwm.stop()
bottom_pwm.stop()
GPIO.cleanup()
    

