import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class DcMotor:
  def __init__(self,Ena, In1A, In2A):
    self.Ena = Ena
    self.In1A = In1A
    self.In2A = In2A
    GPIO.setup(self.Ena, GPIO.OUT)
    GPIO.setup(self.In1A, GPIO.OUT)
    GPIO.setup(self.In2A, GPIO.OUT)
    dc_pwm = GPIO.PWM(self.Ena, 100) # 100 is frequency
    GPIO.output(self.In1A, False)
    GPIO.output(self.In2A, True)
    dc_pwm.start(0)
    
  def forward():
   dc_pwm.ChangeDutyCycle(20)
    GPIO.output(self.Ena, True)

  def stop():
     dc_pwm.stop()
     GPIO.output(self.Ena, False)
    

    
