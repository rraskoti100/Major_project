import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

stepper_pin = [2,3,16,17]

for pin in stepper_pin:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]


#full revolution = 8 cycle
#gear reduction = 1/64
#512 cycle in one complete revolution

for i in range(512):
	for half_step in range(8):
		for pin in stepper_pin:
			GPIO.output(stepper_pin[pin], seq[half_step][pin])
		time.delay(0.001)
GPIO.cleanup()