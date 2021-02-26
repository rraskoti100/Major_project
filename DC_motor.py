import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#setting up enable, In1A, In2A pin
Ena = 15
In1A = 16
in2A = 17

#defining pin 
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1A, GPIO.OUT)
GPIO.setup(In2A, GPIO.OUT)

pwm = GPIO.PWM(Ena, 100) # 100 is frequency

GPIO.output(In1A, True)
GPIO.output(In2A, False)

pwm.start(0)

def forward():
    pwm.ChangeDutyCycle(20)
    GPIO.output(Ena, True)

def main():
    try:
        forward ()
    except KeyBoardInterrupt:
        GPIO.cleanup()
if __name__ = '__main__':
    while True:
        main()
    

