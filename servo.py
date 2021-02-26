import RPi.GPIO as GPIO
from time import sleep

#mode setup for raspberry pi
GPIO.setmode(GPIO.BCM)

#pin setup for servo motor
servo = 2

GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, 50) # 50 is frequency

pwm.start(0)
pwm.ChangeDutyCycle(2.5)
sleep(1)
pwm.ChangeDutyCycle(4)
sleep(1)
pwm.ChangeDutyCycle(5)
sleep(1)

pwm.stop()
GPIO.cleanup()
