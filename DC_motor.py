import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#setting up enable, In1A, In2A pin
Ena = 17
In1A = 27
In2A = 22

#defining pin 
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1A, GPIO.OUT)
GPIO.setup(In2A, GPIO.OUT)

pwm = GPIO.PWM(Ena, 100) # 100 is frequency

GPIO.output(In1A, False)
GPIO.output(In2A, True)

pwm.start(0)

def forward():
    pwm.ChangeDutyCycle(20)
    GPIO.output(Ena, True)

def stop():
    pwm.stop()
    GPIO.output(Ena, False)

if __name__ == '__main__':
    while True:
        try:
            forward ()
            time.sleep(2)
            stop()
            time.sleep(2)
            
        except KeyBoardInterrupt:
            GPIO.cleanup()

    
    

