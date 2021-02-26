import RPi.GPIO as GPIO
from time import sleep, time
GPIO.setmode(GPIO.BCM)


#Setting up echo and trigger pin
TRIG = 18
ECHO = 24

#defining pin as input and output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    GPIO.output(TRIG, True)
    sleep(0.001)
    GPIO.output(TRIG, False)

    if GPIO.input(ECHO) == 0:
        start_time = time()
    if GPIO.input(ECHO) == 1:
        end_time = time()

    dist = ((end_time - start_time)*34300)//2
    return dist

def main():
    try:
        distance = distance()
        print(f"Distance : {distance}")
    except KeyBoardInterrupt:
        GPIO.cleanup()
if __name__ == '__main__':
    while True:
        main()
        
        
