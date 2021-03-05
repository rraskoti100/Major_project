import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class DcMotor:
  def __init__(self,Ena, In1A, In2A):
    self.Ena = Ena
    self.In1A = In1A
    self.In2A = In2A
    GPIO.setup(Ena, GPIO.OUT)
    GPIO.setup(In1A, GPIO.OUT)
    GPIO.setup(In2A, GPIO.OUT)
    dc_pwm = GPIO.PWM(Ena, 100) # 100 is frequency
    
  def forward():
    

    
